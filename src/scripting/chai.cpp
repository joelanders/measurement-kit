// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.

#include <chaiscript/chaiscript.hpp>
#include <chaiscript/chaiscript_stdlib.hpp>
#include <measurement_kit/scripting.hpp>

namespace mk {
namespace scripting {
namespace chai {

Error run(std::string path, std::string script) {
    Engine engine;
    chaiscript::ChaiScript chai(chaiscript::Std_Lib::library(), {}, {path});

    chai.add(chaiscript::fun([&](std::string s) -> std::string {
        return engine.http_request(s);
    }), "_http_request");

    chai.eval_file(script);
    return NoError();
}

} // namespace chai
} // namespace scripting
} // namespace mk
