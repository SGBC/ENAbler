#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging


class SampleCollection(object):
    """a collection of sample"""
    def __init__(self, samples):
        self.samples = samples

    @property
    def logger(self):
        component = "{}.{}".format(type(self).__module__, type(self).__name__)
        return logging.getLogger(component)

    @classmethod
    def parse_sample_file(self, file_path):
        """parse sample file"""
        ext = os.path.splitext(os.path.basename(file_path))[1]
        if ext == '.csv':
            pass
        elif ext == '.txt' or ext == '.tsv' or ext == '.tab':
            pass
        else:
            logger.error(
                f'{ext!r} is not a supported file extension. Aborting')
            sys.exit(1)


class Sample(object):
    """a sample"""
    def __init__(self, header, line):
        info_dict = sample_parser(header, line)
        self.arg = arg

    @staticmethod
    def sample_parser(header, line):
        pass
