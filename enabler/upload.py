#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import gzip
import hashlib
import logging

from enabler import parse


def upload(args):
    """Main function for the `enabler upload` command
    """
    logger = logging.getLogger(__name__)
    logger.debug('Using verbose logger')

    # check if input is a directory
    try:
        input_path = os.path.abspath(args.input)
        assert os.path.isdir(input_path) is True
        file_list = [input_path + '/' + f for f in os.listdir(args.input)]
    except AssertionError as e:
        logger.error(f'--input is not a directory: {args.input}')
        sys.exit(1)
    else:
        for f in file_list:
            try:
                assert os.stat(f).st_size != 0
                if f.endswith('.md5'):
                    continue
            except AssertionError as e:
                logger.error(f'file is empty: {f}')
            else:
                compressed_f = parse.compress(f)
                md5 = parse.calc_md5(compressed_f)
                parse.md5_to_file(compressed_f, md5)
    # TODO
    # - upload with ftp
