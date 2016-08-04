// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.
#ifndef MEASUREMENT_KIT_SCRIPTING_CHAI_HPP
#define MEASUREMENT_KIT_SCRIPTING_CHAI_HPP

#include <measurement_kit/common.hpp>

namespace mk {
namespace scripting {
namespace chai {

Error run(std::string path, std::string script);

} // namespace chai
} // namespace scripting
} // namespace mk
#endif
