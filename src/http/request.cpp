// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.

#include "src/http/request.hpp"

namespace mk {
namespace http {

using namespace mk::net;

void request_connect(Settings settings, Callback<Error, Var<Transport>> transport,
         Var<Reactor> reactor, Var<Logger> logger) {
    request_connect_impl(settings, transport, reactor, logger);
}

void request_send(Var<Transport> transport, Settings settings, Headers headers,
        std::string body, RequestSendCb callback) {
    RequestSerializer serializer;
    try {
        serializer = RequestSerializer(settings, headers, body);
    } catch (Error &error) {
        callback(error);
        return;
    }
    transport->on_error([transport, callback](Error error) {
        transport->on_error(nullptr);
        transport->on_flush(nullptr);
        callback(error);
    });
    transport->on_flush([transport, callback]() {
        transport->on_error(nullptr);
        transport->on_flush(nullptr);
        callback(NoError());
    });
    Buffer buff;
    serializer.serialize(buff);
    transport->write(buff);
}

void request_recv_response(Var<Transport> transport, Callback<Error, Var<Response>> cb,
        Var<Reactor> reactor, Var<Logger> logger) {
    Var<ResponseParserNg> parser(new ResponseParserNg);
    Var<Response> response(new Response);
    Var<bool> prevent_emit(new bool(false));

    transport->on_data([=](Buffer data) { parser->feed(data); });
    parser->on_response([=](Response r) { *response = r; });
    parser->on_body([=](std::string s) { response->body += s; });

    // XXX/TODO: we should improve the parser such that the transport
    // forwards the "error" event to it and then the parser does the right
    // thing, so that the code becomes less "twisted" here.

    parser->on_end([=]() {
        if (*prevent_emit == true) {
            return;
        }
        transport->emit_error(NoError());
    });
    transport->on_error([=](Error err) {
        if (err == EofError()) {
            // Calling parser->on_eof() could trigger parser->on_end() and
            // we don't want this function to call ->emit_error()
            *prevent_emit = true;
            parser->eof();
        }
        // TODO: make sure we remove all cycles
        transport->on_error(nullptr);
        transport->on_data(nullptr);
        reactor->call_soon([=]() {
            logger->debug("request_recv_response: end of closure");
            cb(err, response);
        });
    });
}

void request_sendrecv(Var<Transport> transport, Settings settings,
        Headers headers, std::string body, Callback<Error, Var<Response>> callback,
        Var<Reactor> reactor, Var<Logger> logger) {
    request_send(transport, settings, headers, body, [=](Error error) {
        if (error) {
            callback(error, nullptr);
            return;
        }
        request_recv_response(transport, callback, reactor, logger);
    });
}

void request_cycle(Settings settings, Headers headers, std::string body,
        Callback<Error, Var<Response>> callback, Var<Reactor> reactor, Var<Logger> logger) {
    request_connect(settings, [=](Error err, Var<Transport> transport) {
        if (err) {
            callback(err, nullptr);
            return;
        }
        request_sendrecv(transport, settings, headers, body,
                [callback, transport](Error error, Var<Response> response) {
                    transport->close([callback, error, response]() {
                        callback(error, response);
                    });
                },
                reactor, logger);
    }, reactor, logger);
}

} // namespace http
} // namespace mk
