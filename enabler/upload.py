#!/usr/bin/env python

import os
import hashlib
import logging


def upload(args):
    """Main function for the `enabler upload` command
    """
    logger = logging.getLogger(__name__)
    logger.debug('Using verbose logger')

    # check if input is a directory
    try:
        assert os.path.isdir(os.path.abspath(args.input)) is True
        file_list = [os.path.abspath(f) for f in os.listdir(args.input)]
    except AssertionError as e:
        logger.error('--input is not a directory: %s' % args.input)
    else:
        for f in file_list:
            print(f)
    # TODO here:
    # - compress files
    # - calculate md5
    # - upload with ftp
    # print('hello, world!')
