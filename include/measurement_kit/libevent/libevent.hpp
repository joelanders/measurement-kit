#ifdef MK_INTERNAL
// Part of measurement-kit <https://measurement-kit.github.io/>.
// Measurement-kit is free software. See AUTHORS and LICENSE for more
// information on the copying conditions.
#ifndef MEASUREMENT_KIT_LIBEVENT_LIBEVENT_HPP
#define MEASUREMENT_KIT_LIBEVENT_LIBEVENT_HPP

#include <measurement_kit/dns.hpp>
#include <measurement_kit/net.hpp>

namespace mk {
namespace libevent {

Var<Reactor> make_reactor();

Var<net::Buffer> make_buffer();

void start_read(
    Var<net::Transport> transport,
    Var<net::Buffer> buffer,
    Callback<Error> callback
) noexcept;

void stop_read(Var<net::Transport> transport) noexcept;

void write(
    Var<net::Transport> transport,
    Var<net::Buffer> buffer,
    Callback<Error> callback
) noexcept;

void write(
    Var<net::Transport> transport,
    Var<net::Buffer> buffer
) noexcept;

void close(Var<net::Transport> transport) noexcept;

void connect_tcp(
    std::string address,
    uint16_t port,
    Settings settings,
    Var<Reactor> reactor,
    Var<Logger> logger,
    Callback<
        Error /*error*/,
        Var<Transport> /*transport*/,
        double /*connect_time*/
    > callback
) noexcept;

void connect_ssl(
    Var<Transport> &&transport,
    std::string hostname,
    Settings settings,
    Var<Reactor> reactor,
    Var<Logger> logger,
    Callback<
        Error /*error*/,
        Var<Transport> /*new_transport*/
    > callback
) noexcept;

void query(
    dns::QueryClass dns_class,
    dns::QueryType dns_type,
    std::string name,
    Settings settings,
    Var<Reactor> reactor,
    Var<Logger> logger,
    Callback<
        Error /*error*/,
        Var<dns::Message> /*message*/
    > callback
) noexcept;

} // namespace libevent
} // namespace mk
#endif // MEASUREMENT_KIT_LIBEVENT_LIBEVENT_HPP
#endif // MK_INTERNAL
