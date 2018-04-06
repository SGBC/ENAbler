#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""General file reading utilities for the enabler program"""

import os
import gzip
import hashlib
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
            logger.info(f'{infile} is not gzipped')
            return False
        else:
            logger.debug(f'{infile} is gzipped')
            return True


def calc_md5(infile, block_size=256*128):
    """Calculate the md5sum of a file

    Args:
        infile (str): input file
        block_size (int): block_size for the file chunks. Default = 256*128

    Returns:
        str: md5 sum of the inout file
    """
    logger = logging.getLogger(__name__)
    logger.info(f'Calculating md5 of {infile}')
    md5 = hashlib.md5()
    with open(infile, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def md5_to_file(infile, md5):
    """Write md5 to a file
    """
    logger = logging.getLogger(__name__)
    if not os.path.exists(infile + '.md5'):
        with open(infile + '.md5', 'w') as outfile:
            filename = infile.split('/')[-1]
            string = md5 + '  ' + filename + '\n'
            outfile.write(string)
    else:
        logger.debug(f'{infile}.md5 already exists')


def compress(infile):
    """Gzip a file
    """
    if is_gzipped(infile):
        return infile
    else:
        outfile = infile + '.gz'
        with open(infile, 'rb') as i, gzip.open(outfile, 'wb') as o:
            o.writelines(i)
        return outfile
