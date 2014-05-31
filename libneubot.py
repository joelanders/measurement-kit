#
# LibIght interface - Public domain.
# WARNING: Autogenerated file - do not edit!
#

# pylint: disable = C0111, C0103

import _ctypes
import ctypes
import logging
import os
import sys

if sys.platform == "darwin":
    LIBIGHT_NAME = "/usr/local/lib/libneubot.dylib.3"
else:
    LIBIGHT_NAME = "/usr/local/lib/libneubot.so.3"

LIBIGHT = ctypes.CDLL(LIBIGHT_NAME)

DIE = getattr(os, '_exit')

IGHT_SLOT_VO = ctypes.CFUNCTYPE(None, ctypes.py_object)

IGHT_HOOK_VO = ctypes.CFUNCTYPE(None, ctypes.py_object)
IGHT_HOOK_VOS = ctypes.CFUNCTYPE(None, ctypes.py_object,
  ctypes.c_char_p)

class ConnectionBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class EchoServerBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class PollableBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class PollerBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class ProtocolBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_

class StringVectorBase(object):

    def __init__(self):
        self.context_ = None
        self.voidp_ = None

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, cls):
            raise RuntimeError('invalid cast')
        if not obj.voidp_:
            obj.voidp_ = ctypes.c_void_p(obj.context_)
        return obj.voidp_



LIBIGHT.IghtConnection_attach.restype = ctypes.c_void_p
LIBIGHT.IghtConnection_attach.argtypes = (
    ProtocolBase,
    ctypes.c_longlong,
)



LIBIGHT.IghtConnection_connect.restype = ctypes.c_void_p
LIBIGHT.IghtConnection_connect.argtypes = (
    ProtocolBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBIGHT.IghtConnection_connect_hostname.restype = ctypes.c_void_p
LIBIGHT.IghtConnection_connect_hostname.argtypes = (
    ProtocolBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBIGHT.IghtConnection_get_protocol.restype = ctypes.c_void_p
LIBIGHT.IghtConnection_get_protocol.argtypes = (
    ConnectionBase,
)



LIBIGHT.IghtConnection_set_timeout.restype = ctypes.c_int
LIBIGHT.IghtConnection_set_timeout.argtypes = (
    ConnectionBase,
    ctypes.c_double,
)



LIBIGHT.IghtConnection_clear_timeout.restype = ctypes.c_int
LIBIGHT.IghtConnection_clear_timeout.argtypes = (
    ConnectionBase,
)



LIBIGHT.IghtConnection_start_tls.restype = ctypes.c_int
LIBIGHT.IghtConnection_start_tls.argtypes = (
    ConnectionBase,
    ctypes.c_uint,
)



LIBIGHT.IghtConnection_read.restype = ctypes.c_int
LIBIGHT.IghtConnection_read.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_readline.restype = ctypes.c_int
LIBIGHT.IghtConnection_readline.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_readn.restype = ctypes.c_int
LIBIGHT.IghtConnection_readn.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_discardn.restype = ctypes.c_int
LIBIGHT.IghtConnection_discardn.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_write.restype = ctypes.c_int
LIBIGHT.IghtConnection_write.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_puts.restype = ctypes.c_int
LIBIGHT.IghtConnection_puts.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
)



LIBIGHT.IghtConnection_write_rand.restype = ctypes.c_int
LIBIGHT.IghtConnection_write_rand.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_write_readbuf.restype = ctypes.c_int
LIBIGHT.IghtConnection_write_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_puts_readbuf.restype = ctypes.c_int
LIBIGHT.IghtConnection_puts_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_char_p,
)



LIBIGHT.IghtConnection_write_rand_readbuf.restype = ctypes.c_int
LIBIGHT.IghtConnection_write_rand_readbuf.argtypes = (
    ConnectionBase,
    ctypes.c_size_t,
)



LIBIGHT.IghtConnection_read_into_.restype = ctypes.c_int
LIBIGHT.IghtConnection_read_into_.argtypes = (
    ConnectionBase,
    ctypes.c_void_p,
)



LIBIGHT.IghtConnection_write_from_.restype = ctypes.c_int
LIBIGHT.IghtConnection_write_from_.argtypes = (
    ConnectionBase,
    ctypes.c_void_p,
)



LIBIGHT.IghtConnection_enable_read.restype = ctypes.c_int
LIBIGHT.IghtConnection_enable_read.argtypes = (
    ConnectionBase,
)



LIBIGHT.IghtConnection_disable_read.restype = ctypes.c_int
LIBIGHT.IghtConnection_disable_read.argtypes = (
    ConnectionBase,
)



LIBIGHT.IghtConnection_close.argtypes = (
    ConnectionBase,
)



LIBIGHT.IghtEchoServer_construct.restype = ctypes.c_void_p
LIBIGHT.IghtEchoServer_construct.argtypes = (
    PollerBase,
    ctypes.c_int,
    ctypes.c_char_p,
    ctypes.c_char_p,
)



LIBIGHT.IghtPollable_construct.restype = ctypes.c_void_p
LIBIGHT.IghtPollable_construct.argtypes = (
    PollerBase,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    ctypes.py_object,
)

def IghtPollable_handle_read_slot_vo(selfptr):
    try:
        selfptr.handle_read()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLABLE_HANDLE_READ_SLOT_VO = IGHT_SLOT_VO(
    IghtPollable_handle_read_slot_vo
)

def IghtPollable_handle_write_slot_vo(selfptr):
    try:
        selfptr.handle_write()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLABLE_HANDLE_WRITE_SLOT_VO = IGHT_SLOT_VO(
    IghtPollable_handle_write_slot_vo
)

def IghtPollable_handle_error_slot_vo(selfptr):
    try:
        selfptr.handle_error()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLABLE_HANDLE_ERROR_SLOT_VO = IGHT_SLOT_VO(
    IghtPollable_handle_error_slot_vo
)



LIBIGHT.IghtPollable_attach.restype = ctypes.c_int
LIBIGHT.IghtPollable_attach.argtypes = (
    PollableBase,
    ctypes.c_longlong,
)



LIBIGHT.IghtPollable_detach.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_get_fileno.restype = ctypes.c_longlong
LIBIGHT.IghtPollable_get_fileno.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_set_readable.restype = ctypes.c_int
LIBIGHT.IghtPollable_set_readable.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_unset_readable.restype = ctypes.c_int
LIBIGHT.IghtPollable_unset_readable.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_set_writable.restype = ctypes.c_int
LIBIGHT.IghtPollable_set_writable.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_unset_writable.restype = ctypes.c_int
LIBIGHT.IghtPollable_unset_writable.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_set_timeout.argtypes = (
    PollableBase,
    ctypes.c_double,
)



LIBIGHT.IghtPollable_clear_timeout.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPollable_close.argtypes = (
    PollableBase,
)



LIBIGHT.IghtPoller_construct.restype = ctypes.c_void_p
LIBIGHT.IghtPoller_construct.argtypes = (
)



LIBIGHT.IghtPoller_sched.restype = ctypes.c_int
LIBIGHT.IghtPoller_sched.argtypes = (
    PollerBase,
    ctypes.c_double,
    IGHT_HOOK_VO,
    ctypes.py_object,
)

def IghtPoller_sched_callback_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["callback"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_SCHED_CALLBACK_HOOK_VO = IGHT_HOOK_VO(
    IghtPoller_sched_callback_hook_vo
)



LIBIGHT.IghtPoller_defer_read.restype = ctypes.c_int
LIBIGHT.IghtPoller_defer_read.argtypes = (
    PollerBase,
    ctypes.c_longlong,
    IGHT_HOOK_VO,
    IGHT_HOOK_VO,
    ctypes.py_object,
    ctypes.c_double,
)

def IghtPoller_defer_read_handle_ok_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_ok"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_DEFER_READ_HANDLE_OK_HOOK_VO = IGHT_HOOK_VO(
    IghtPoller_defer_read_handle_ok_hook_vo
)

def IghtPoller_defer_read_handle_timeout_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_timeout"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_DEFER_READ_HANDLE_TIMEOUT_HOOK_VO = IGHT_HOOK_VO(
    IghtPoller_defer_read_handle_timeout_hook_vo
)



LIBIGHT.IghtPoller_defer_write.restype = ctypes.c_int
LIBIGHT.IghtPoller_defer_write.argtypes = (
    PollerBase,
    ctypes.c_longlong,
    IGHT_HOOK_VO,
    IGHT_HOOK_VO,
    ctypes.py_object,
    ctypes.c_double,
)

def IghtPoller_defer_write_handle_ok_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_ok"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_DEFER_WRITE_HANDLE_OK_HOOK_VO = IGHT_HOOK_VO(
    IghtPoller_defer_write_handle_ok_hook_vo
)

def IghtPoller_defer_write_handle_timeout_hook_vo(closure):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["handle_timeout"](closure.opaque)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_DEFER_WRITE_HANDLE_TIMEOUT_HOOK_VO = IGHT_HOOK_VO(
    IghtPoller_defer_write_handle_timeout_hook_vo
)



LIBIGHT.IghtPoller_resolve.restype = ctypes.c_int
LIBIGHT.IghtPoller_resolve.argtypes = (
    PollerBase,
    ctypes.c_char_p,
    ctypes.c_char_p,
    IGHT_HOOK_VOS,
    ctypes.py_object,
)

def IghtPoller_resolve_callback_hook_vos(closure, string):
    _ctypes.Py_DECREF(closure)
    try:
        closure.functions["callback"](closure.opaque, string)
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPOLLER_RESOLVE_CALLBACK_HOOK_VOS = IGHT_HOOK_VOS(
    IghtPoller_resolve_callback_hook_vos
)



LIBIGHT.IghtPoller_loop.argtypes = (
    PollerBase,
)



LIBIGHT.IghtPoller_break_loop.argtypes = (
    PollerBase,
)



LIBIGHT.IghtProtocol_construct.restype = ctypes.c_void_p
LIBIGHT.IghtProtocol_construct.argtypes = (
    PollerBase,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    IGHT_SLOT_VO,
    ctypes.py_object,
)

def IghtProtocol_handle_connect_slot_vo(selfptr):
    try:
        selfptr.handle_connect()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_CONNECT_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_connect_slot_vo
)

def IghtProtocol_handle_ssl_slot_vo(selfptr):
    try:
        selfptr.handle_ssl()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_SSL_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_ssl_slot_vo
)

def IghtProtocol_handle_data_slot_vo(selfptr):
    try:
        selfptr.handle_data()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_DATA_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_data_slot_vo
)

def IghtProtocol_handle_flush_slot_vo(selfptr):
    try:
        selfptr.handle_flush()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_FLUSH_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_flush_slot_vo
)

def IghtProtocol_handle_eof_slot_vo(selfptr):
    try:
        selfptr.handle_eof()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_EOF_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_eof_slot_vo
)

def IghtProtocol_handle_error_slot_vo(selfptr):
    try:
        selfptr.handle_error()
    except (KeyboardInterrupt, SystemExit):
        DIE(0)
    except:
        logging.error("Unhandled exception", exc_info=1)
        DIE(1)

IGHTPROTOCOL_HANDLE_ERROR_SLOT_VO = IGHT_SLOT_VO(
    IghtProtocol_handle_error_slot_vo
)



LIBIGHT.IghtProtocol_get_poller.restype = ctypes.c_void_p
LIBIGHT.IghtProtocol_get_poller.argtypes = (
    ProtocolBase,
)



LIBIGHT.IghtProtocol_destruct.argtypes = (
    ProtocolBase,
)



LIBIGHT.IghtStringVector_construct.restype = ctypes.c_void_p
LIBIGHT.IghtStringVector_construct.argtypes = (
    PollerBase,
    ctypes.c_size_t,
)



LIBIGHT.IghtStringVector_append.restype = ctypes.c_int
LIBIGHT.IghtStringVector_append.argtypes = (
    StringVectorBase,
    ctypes.c_char_p,
)



LIBIGHT.IghtStringVector_get_poller.restype = ctypes.c_void_p
LIBIGHT.IghtStringVector_get_poller.argtypes = (
    StringVectorBase,
)



LIBIGHT.IghtStringVector_get_next.restype = ctypes.c_char_p
LIBIGHT.IghtStringVector_get_next.argtypes = (
    StringVectorBase,
)



LIBIGHT.IghtStringVector_destruct.argtypes = (
    StringVectorBase,
)



class IghtHookClosure(object):
    def __init__(self):
        self.opaque = None
        self.functions = {}



class Connection(ConnectionBase):

    def __init__(self):
        ConnectionBase.__init__(self)
        self.context_ = None

    @staticmethod
    def attach(protocol, filenum):
        self = Connection()
        self.context_ = LIBIGHT.IghtConnection_attach(protocol, filenum)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        self.protocol = protocol
        return self

    @staticmethod
    def connect(protocol, family, address, port):
        self = Connection()
        self.context_ = LIBIGHT.IghtConnection_connect(protocol, family,
          address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        self.protocol = protocol
        return self

    @staticmethod
    def connect_hostname(protocol, family, address, port):
        self = Connection()
        self.context_ = LIBIGHT.IghtConnection_connect_hostname(protocol,
          family, address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        self.protocol = protocol
        return self

    def get_protocol(self):
        return self.protocol

    def set_timeout(self, timeo):
        return LIBIGHT.IghtConnection_set_timeout(self, timeo)

    def clear_timeout(self):
        return LIBIGHT.IghtConnection_clear_timeout(self)

    def start_tls(self, server_side):
        return LIBIGHT.IghtConnection_start_tls(self, server_side)

    def read(self, base, count):
        return LIBIGHT.IghtConnection_read(self, base, count)

    def readline(self, base, count):
        return LIBIGHT.IghtConnection_readline(self, base, count)

    def readn(self, base, count):
        return LIBIGHT.IghtConnection_readn(self, base, count)

    def discardn(self, count):
        return LIBIGHT.IghtConnection_discardn(self, count)

    def write(self, base, count):
        return LIBIGHT.IghtConnection_write(self, base, count)

    def puts(self, base):
        return LIBIGHT.IghtConnection_puts(self, base)

    def write_rand(self, count):
        return LIBIGHT.IghtConnection_write_rand(self, count)

    def write_readbuf(self, base, count):
        return LIBIGHT.IghtConnection_write_readbuf(self, base, count)

    def puts_readbuf(self, base):
        return LIBIGHT.IghtConnection_puts_readbuf(self, base)

    def write_rand_readbuf(self, count):
        return LIBIGHT.IghtConnection_write_rand_readbuf(self, count)

    def read_into_(self, evdest):
        return LIBIGHT.IghtConnection_read_into_(self, evdest)

    def write_from_(self, evsource):
        return LIBIGHT.IghtConnection_write_from_(self, evsource)

    def enable_read(self):
        return LIBIGHT.IghtConnection_enable_read(self)

    def disable_read(self):
        return LIBIGHT.IghtConnection_disable_read(self)

    def close(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBIGHT.IghtConnection_close(self)
        self.context_ = None



class EchoServer(EchoServerBase):

    def __init__(self, poller, use_ipv6, address, port):
        EchoServerBase.__init__(self)
        self.context_ = LIBIGHT.IghtEchoServer_construct(poller, use_ipv6,
          address, port)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)



class Pollable(PollableBase):

    def handle_read(self):
        pass

    def handle_write(self):
        pass

    def handle_error(self):
        pass

    def __init__(self, poller):
        PollableBase.__init__(self)
        self.context_ = LIBIGHT.IghtPollable_construct(poller,
          IGHTPOLLABLE_HANDLE_READ_SLOT_VO, IGHTPOLLABLE_HANDLE_WRITE_SLOT_VO,
          IGHTPOLLABLE_HANDLE_ERROR_SLOT_VO, self)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def attach(self, filenum):
        return LIBIGHT.IghtPollable_attach(self, filenum)

    def detach(self):
        LIBIGHT.IghtPollable_detach(self)

    def get_fileno(self):
        return LIBIGHT.IghtPollable_get_fileno(self)

    def set_readable(self):
        return LIBIGHT.IghtPollable_set_readable(self)

    def unset_readable(self):
        return LIBIGHT.IghtPollable_unset_readable(self)

    def set_writable(self):
        return LIBIGHT.IghtPollable_set_writable(self)

    def unset_writable(self):
        return LIBIGHT.IghtPollable_unset_writable(self)

    def set_timeout(self, delta):
        LIBIGHT.IghtPollable_set_timeout(self, delta)

    def clear_timeout(self):
        LIBIGHT.IghtPollable_clear_timeout(self)

    def close(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBIGHT.IghtPollable_close(self)
        self.context_ = None



class Poller(PollerBase):

    def __init__(self):
        PollerBase.__init__(self)
        self.context_ = LIBIGHT.IghtPoller_construct()
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)

    def sched(self, delta, callback, opaque):

        closure = IghtHookClosure()
        closure.functions['callback'] = callback
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBIGHT.IghtPoller_sched(self, delta,
          IGHTPOLLER_SCHED_CALLBACK_HOOK_VO, closure)

    def defer_read(self, fileno, handle_ok, handle_timeout, opaque, timeout):

        closure = IghtHookClosure()
        closure.functions['handle_ok'] = handle_ok
        closure.functions['handle_timeout'] = handle_timeout
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBIGHT.IghtPoller_defer_read(self, fileno,
          IGHTPOLLER_DEFER_READ_HANDLE_OK_HOOK_VO,
          IGHTPOLLER_DEFER_READ_HANDLE_TIMEOUT_HOOK_VO, closure, timeout)

    def defer_write(self, fileno, handle_ok, handle_timeout, opaque,
          timeout):

        closure = IghtHookClosure()
        closure.functions['handle_ok'] = handle_ok
        closure.functions['handle_timeout'] = handle_timeout
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBIGHT.IghtPoller_defer_write(self, fileno,
          IGHTPOLLER_DEFER_WRITE_HANDLE_OK_HOOK_VO,
          IGHTPOLLER_DEFER_WRITE_HANDLE_TIMEOUT_HOOK_VO, closure, timeout)

    def resolve(self, family, name, callback, opaque):

        closure = IghtHookClosure()
        closure.functions['callback'] = callback
        closure.opaque = opaque
        _ctypes.Py_INCREF(closure)

        return LIBIGHT.IghtPoller_resolve(self, family, name,
          IGHTPOLLER_RESOLVE_CALLBACK_HOOK_VOS, closure)

    def loop(self):
        LIBIGHT.IghtPoller_loop(self)

    def break_loop(self):
        LIBIGHT.IghtPoller_break_loop(self)



class Protocol(ProtocolBase):

    def handle_connect(self):
        pass

    def handle_ssl(self):
        pass

    def handle_data(self):
        pass

    def handle_flush(self):
        pass

    def handle_eof(self):
        pass

    def handle_error(self):
        pass

    def __init__(self, poller):
        ProtocolBase.__init__(self)
        self.context_ = LIBIGHT.IghtProtocol_construct(poller,
          IGHTPROTOCOL_HANDLE_CONNECT_SLOT_VO, IGHTPROTOCOL_HANDLE_SSL_SLOT_VO,
          IGHTPROTOCOL_HANDLE_DATA_SLOT_VO, IGHTPROTOCOL_HANDLE_FLUSH_SLOT_VO,
          IGHTPROTOCOL_HANDLE_EOF_SLOT_VO, IGHTPROTOCOL_HANDLE_ERROR_SLOT_VO,
          self)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        self.poller = poller

    def get_poller(self):
        return self.poller

    def destruct(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBIGHT.IghtProtocol_destruct(self)
        self.context_ = None



class StringVector(StringVectorBase):

    def __init__(self, poller, count):
        StringVectorBase.__init__(self)
        self.context_ = LIBIGHT.IghtStringVector_construct(poller, count)
        if not self.context_:
            DIE(1)
        _ctypes.Py_INCREF(self)
        self.poller = poller

    def append(self, str):
        return LIBIGHT.IghtStringVector_append(self, str)

    def get_poller(self):
        return self.poller

    def get_next(self):
        return LIBIGHT.IghtStringVector_get_next(self)

    def destruct(self):
        if not self.context_:
            return
        _ctypes.Py_DECREF(self)
        LIBIGHT.IghtStringVector_destruct(self)
        self.context_ = None

