// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.
#ifndef MEASUREMENT_KIT_SCRIPTING_ERROR_HPP
#define MEASUREMENT_KIT_SCRIPTING_ERROR_HPP

#include <measurement_kit/common/error.hpp>
#include <measurement_kit/net/buffer.hpp>

namespace mk {
namespace scripting {

MK_DEFINE_ERR(MK_ERR_SCRIPTING(0), ScriptingKeyError, "")
MK_DEFINE_ERR(MK_ERR_SCRIPTING(1), ScriptingTypeError, "")
MK_DEFINE_ERR(MK_ERR_SCRIPTING(2), ScriptingUnmarshalError, "")

} // namespace scripting
} // namespace mk
#endif
