#!/usr/bin/env python

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
        logger.error('--input is not a directory: %s' % args.input)
        sys.exit(1)
    else:
        for f in file_list:
            try:
                assert os.stat(f).st_size != 0
            except AssertionError as e:
                logger.error('file is empty: %s' % f)
            else:
                compressed_f = compress(f)
                md5 = parse.calc_md5(compressed_f)
    # TODO
    # - upload with ftp


def compress(infile):
    """Gzip a file
    """
    if parse.is_gzipped(infile):
        return infile
    else:
        outfile = infile + '.gz'
        with open(infile, 'rb') as i, gzip.open(outfile, 'wb') as o:
            o.writelines(i)
        return outfile
