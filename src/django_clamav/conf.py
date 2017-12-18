import os
from django.conf import settings as _settings


# Unix socket of clamd. If not provided we will guess.
CLAMAV_UNIX_SOCKET = getattr(_settings, 'CLAMAV_UNIX_SOCKET', None)

if CLAMAV_UNIX_SOCKET is None:
    if os.path.exists('/var/run/clamd.scan/'):
        # Fedora, CentOS
        CLAMAV_UNIX_SOCKET = '/var/run/clamd.scan/clamd.sock'
    else:
        # This is default for Ubuntu, Debian based distros
        CLAMAV_UNIX_SOCKET = '/var/run/clamav/clamd.ctl'

# If you want to use TCP socket set this to True
CLAMAV_USE_TCP = getattr(_settings, 'CLAMAV_USE_TCP', False)

# Default clamd TCP socket port
CLAMAV_TCP_PORT = getattr(_settings, 'CLAMAV_TCP_PORT', 3310)
# Default clamd TCP socket address
CLAMAV_TCP_ADDR = getattr(_settings, 'CLAMAV_TCP_ADDR', '127.0.0.1')

# Enable clamd scanner. By default True. Set to False only for development.
CLAMAV_ENABLED = getattr(_settings, 'CLAMAV_ENABLED', True)
