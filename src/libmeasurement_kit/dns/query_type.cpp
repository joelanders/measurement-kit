// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software under the BSD license. See AUTHORS
// and LICENSE for more information on the copying conditions.

#include <measurement_kit/dns.hpp>

namespace mk {
namespace dns {

#define XX(_name)                                                              \
    if (s == #_name) {                                                         \
        return MK_DNS_TYPE_##_name;                                           \
    }
QueryTypeId query_type_ids_(std::string s) {
    MK_DNS_TYPE_IDS
    return MK_DNS_TYPE_INVALID;
}
#undef XX

} // namespace dns
} // namespace mk
