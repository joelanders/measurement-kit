// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.
#ifndef MEASUREMENT_KIT_SCRIPTING_ENGINE_HPP
#define MEASUREMENT_KIT_SCRIPTING_ENGINE_HPP

#include <measurement_kit/common.hpp>
#include <thread>

namespace mk {
namespace scripting {

class Engine {
  public:
    Engine();
    ~Engine();

    void http_request(std::string args, Callback<std::string> callback);
    std::string http_request(std::string args);

  private:
    Var<Reactor> reactor = Reactor::make();
    Var<Logger> logger = Logger::make();
    std::thread thread;
};

} // namespace scripting
} // namespace mk
#endif
