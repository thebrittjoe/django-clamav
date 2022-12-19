import logging

from django.core.exceptions import ValidationError

from django_clamav import get_scanner
from .conf import CLAMAV_ENABLED


logger = logging.getLogger(__name__)


def validate_file_infection(file):

    # If django-clamav is disabled then do not check the file.
    if not CLAMAV_ENABLED:
        return

    # Ensure file pointer is at beginning of the file
    file.seek(0)

    scanner = get_scanner()
    try:
        result = scanner.instream(file)
    except IOError:
        # Ping the server if it fails than the server is down
        scanner.ping()
        # Server is up. This means that the file is too big.
        logger.warning('The file is too large for ClamD to scan it. Bytes Read {}'.format(file.tell()))
        file.seek(0)
        return

    if result and result['stream'][0] == 'FOUND':
        raise ValidationError(_('File is infected with malware'), code='infected')

    # Return file pointer to beginning of the file again
    file.seek(0)
