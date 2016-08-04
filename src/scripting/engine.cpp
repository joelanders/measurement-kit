// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.

#include <future>
#include <measurement_kit/ext.hpp>
#include <measurement_kit/http.hpp>
#include <measurement_kit/scripting.hpp>

namespace mk {
namespace scripting {

using Object = nlohmann::json;

Engine::Engine() {
    //logger->set_verbosity(16);
    std::promise<bool> promise;
    std::future<bool> future = promise.get_future();
    // WARNING: below we're passing `this` to the thread, which means that
    // the destructor MUST wait the thread. Otherwise, when the thread dies
    // many strange things could happen (I have seen SIGABRT).
    thread = std::thread([&]() {
        reactor->loop_with_initial_event([&]() {
            promise.set_value(true);
        });
    });
    future.wait();
}

Engine::~Engine() {
    reactor->break_loop();
    thread.join();
}

static Object make_error(Error err) {
    Object result = Object::array();
    Object obj = Object::object();
    obj["code"] = err.code;
    obj["reason"] = err.reason;
    result.push_back(obj);
    obj = Object::object();
    result.push_back(obj);
    return result;
}

void Engine::http_request(std::string args, Callback<std::string> callback) {
    reactor->call_soon([=]() {
        try {
            Object root = Object::parse(args);

            Object obj = root.at("settings");
            Settings settings;
            for (Object::iterator it = obj.begin(); it != obj.end(); ++it) {
                settings[it.key()] = it.value().get<std::string>();
            }

            obj = root.at("headers");
            http::Headers headers;
            for (Object::iterator it = obj.begin(); it != obj.end(); ++it) {
                headers[it.key()] = it.value();
            }

            std::string body = root.at("body");

            http::request(settings, headers, body,
                          [=](Error error, Var<http::Response> resp) {

                              Object result = Object::array();
                              Object obj = Object::object();

                              obj["code"] = error.code;
                              obj["reason"] = error.reason;
                              result.push_back(obj);

                              obj = Object::object();
                              if (resp) {
                                  obj["response_line"] = resp->response_line;
                                  obj["http_major"] = resp->http_major;
                                  obj["http_minor"] = resp->http_minor;
                                  obj["status_code"] = resp->status_code;
                                  obj["reason"] = resp->reason;
                                  obj["headers"] = resp->headers;
                                  obj["body"] = resp->body;
                              }
                              result.push_back(obj);

                              callback(result.dump());
                          }, reactor, logger);

        } catch (std::out_of_range &) {
            callback(make_error(ScriptingKeyError()));
        } catch (std::domain_error &) {
            callback(make_error(ScriptingTypeError()));
        }
    });
}

std::string Engine::http_request(std::string args) {
    std::promise<std::string> promise;
    std::future<std::string> future = promise.get_future();
    http_request(args, [&](std::string result) {
        promise.set_value(result);
    });
    return future.get();
}

} // namespace scripting
} // namespace mk
