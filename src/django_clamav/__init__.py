

def get_scanner():
    """Lazy get scanner configured scanner when needed"""
    import clamd
    from . import conf

    if conf.CLAMAV_USE_TCP:
        return clamd.ClamdNetworkSocket(conf.CLAMAV_TCP_ADDR, conf.CLAMAV_TCP_PORT)

    return clamd.ClamdUnixSocket(conf.CLAMAV_UNIX_SOCKET)
