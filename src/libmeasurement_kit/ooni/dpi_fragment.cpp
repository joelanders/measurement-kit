// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software under the BSD license. See AUTHORS
// and LICENSE for more information on the copying conditions.

#include "src/libmeasurement_kit/ooni/constants.hpp"
#include "src/libmeasurement_kit/ooni/utils.hpp"
#include "src/libmeasurement_kit/ooni/ssl_filter.hpp"
#include "src/libmeasurement_kit/common/fcompose.hpp"
#include "src/libmeasurement_kit/common/utils.hpp"
#include <measurement_kit/ooni.hpp>
#include <stdio.h>
#include <unistd.h>

namespace mk {
namespace ooni {

using namespace mk::report;

std::string fragmented_https_request(bool do_fragment, bool do_ssl,
                        SharedPtr<Logger> logger) {
    std::string hostname { "example.com" };
    std::string ip { "93.184.216.34" };

    SharedPtr<std::string> nread(new std::string);
    SharedPtr<std::string> nwrite(new std::string);
    SharedPtr<std::string> aread(new std::string);
    SharedPtr<std::string> awrite(new std::string);

    SSL_CTX* ctx = SSL_CTX_new(SSLv23_method()); //XXX don't ignore errors
    if (ctx == NULL) {
        logger->info("failed to make context\n");
        exit(1);
    }   
    SSL_CTX_set_verify(ctx, SSL_VERIFY_NONE, NULL); //XXX probably want to verify eventually

    SSLFilter ssl_filter = SSLFilter(ctx, nread, nwrite, aread, awrite, hostname);
    if (!do_ssl) { //XXX v. hacky; make passthrough class
        awrite = nwrite;
        aread = nread;
    }

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
    {
        logger->info("socket() failed");
        return *aread; //XXX probably raise exception
    }

    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    if (do_ssl) {
        serv_addr.sin_port = htons(443);
    } else {
        serv_addr.sin_port = htons(80);
    }

    if (inet_pton(AF_INET, ip.c_str(), &serv_addr.sin_addr) <= 0) {
        logger->info("inet_pton() failed");
        return *aread; //XXX probably raise exception
    }

    if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        logger->info("connect() failed");
        return *aread; //XXX probably raise exception
    }

    *awrite = "GET /index.html HTTP/1.1\r\nHost: ";
    *awrite += hostname;
    *awrite += "\r\n\r\n";
    if (do_ssl) { //XXX hacky; make a proper passthrough class
        ssl_filter.update();
    }

    char readbuf[1024]; //XXX put on heap

    struct timeval tv;
    int sel_ret;
    int n;
    bool stop_reading = false;
    bool stop_writing = false;
    fd_set rfds, wfds;

    while(1) {
        logger->info("TOP OF WHILE LOOP\n");
        FD_ZERO(&rfds);
        FD_ZERO(&wfds);
        if (!stop_reading) {
            FD_SET(sockfd, &rfds);
            logger->info("we want to read");
        }
        if (!nwrite->empty() && !stop_writing) {
            FD_SET(sockfd, &wfds);
            logger->info("we want to write");
        }

        tv.tv_sec = 4;
        tv.tv_usec = 0;

        logger->info("BLOCKING ON SELECT\n");
        sel_ret = select(sockfd+1, &rfds, &wfds, NULL, &tv);
        if (sel_ret < 0) {
            logger->info("select() failed");
            break;
        }
        if (sel_ret == 0) {
            logger->info("select() timed out.\n");
            if (do_ssl) {
                ssl_filter.update(); //XXX shouldn't need to sprinkle these around so much if i do more thinking
            }
            break;
        }
        if (FD_ISSET(sockfd, &wfds)) {
            logger->info("WRITABLE\n");

            //XXX clean this up
            if (do_fragment) {
                std::size_t found = nwrite->find(hostname);
                if (found!=std::string::npos) {
                    logger->info("$$$$$$ found plaintext hostname; hacking planet $$$$$$$$$");
                    n = write(sockfd, nwrite->c_str(), found+3);
                    if (n > 0) {
                        nwrite->erase(0, n);
                    }
                    sleep(0.5);
                }
            }

            n = write(sockfd, nwrite->c_str(), nwrite->length());
            if (n > 0) {
                nwrite->erase(0, n);
            }
        }

        if (FD_ISSET(sockfd, &rfds)) {
            logger->info("READABLE\n");
            while(1) {
                n = read(sockfd, &readbuf, sizeof(readbuf));
                logger->info("read from sockfd: %d", n);
                if (read > 0) {
                    size_t cur_size = nread->length();
                    nread->resize(cur_size + n);
                    std::copy(readbuf, readbuf + n, nread->begin() + cur_size);
                }
                if (n == 0) {
                    stop_reading = true;
                    break;
                }
                if (static_cast<size_t>(n) != sizeof(readbuf)) {
                    break;
                }
                if(n < 0) {
                    break;
                }
            }
        }

        if (do_ssl) {
            ssl_filter.update();
        }
        if (awrite->size() == 0 && nwrite->size() == 0) {
            stop_writing = true;
        }
        if (stop_reading && stop_writing) {
            break;
        }

    }

    return *aread;
}

void dpi_fragment(Settings options, Callback<SharedPtr<report::Entry>> callback,
                        SharedPtr<Reactor> reactor, SharedPtr<Logger> logger) {
    reactor->call_in_thread(logger, [callback = std::move(callback),
                                     logger = std::move(logger),
                                     reactor = std::move(reactor)]() {
        logger->info("starting dpi_fragment");
        SharedPtr<Entry> entry(new Entry);

        std::string fragmented_https = fragmented_https_request(true, true, logger);
        std::string unfragmented_https = fragmented_https_request(false, true, logger);
        std::string fragmented_http = fragmented_https_request(true, false, logger);
        std::string unfragmented_http = fragmented_https_request(false, false, logger);

        logger->info("fragmented https response: %s", fragmented_https.c_str());
        logger->info("unfragmented https response: %s", unfragmented_https.c_str());
        logger->info("fragmented http response: %s", fragmented_http.c_str());
        logger->info("unfragmented http response: %s", unfragmented_http.c_str());

        logger->info("fragmented https response length: %d", fragmented_https.length());
        logger->info("unfragmented https response length: %d", unfragmented_https.length());
        logger->info("fragmented http response length: %d", fragmented_http.length());
        logger->info("unfragmented http response length: %d", unfragmented_http.length());
        reactor->call_soon([entry = std::move(entry),
                            callback = std::move(callback)]() {
            callback(entry);
        });
    });
}

} // namespace ooni
} // namespace mk
