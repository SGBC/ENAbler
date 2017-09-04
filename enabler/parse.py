#!/usr/bin/env python

"""General file reading utilities for the enabler program"""

import logging


def is_gzipped(infile):
    """Check in a file is in gzip format or not
    """
    logger = logging.getLogger(__name__)

    magic_number = b'\x1f\x8b'
    f = open(infile, 'rb')
    with f:
        try:
            assert f.read(2) == magic_number
        except AssertionError as e:
            logger.info('%s is not gzipped' % infile)
            return False
        else:
            logger.debug('%s is gzipped' % infile)
            return True
