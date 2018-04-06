#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import sys
import copy
import logging


class SampleCollection(object):
    """a collection of sample"""
    def __init__(self, sample_file):
        self.sample_file = sample_file
        self.samples = []
        self.parse_sample_file(self.sample_file)

    @property
    def logger(self):
        component = f'{type(self).__module__}.{type(self).__name__}'
        return logging.getLogger(component)

    @classmethod
    def parse_sample_file(self, file_path):
        """parse sample file"""
        ext = os.path.splitext(os.path.basename(file_path))[1]
        if ext == '.csv':
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                header = reader.__next__()
                for line in reader:
                    self.samples.append(Sample(header, line))
        # elif ext == '.txt' or ext == '.tsv' or ext == '.tab':
        #     pass
        else:
            logger.error(
                f'{ext!r} is not a supported file extension. Aborting')
            sys.exit(1)


class Sample(object):
    """a sample"""
    def __init__(self, header, line):
        self.init_sample(header, line)

    @classmethod
    def init_sample(self, header, line):
        sample_dict = {field: value for field, value in zip(header, line)}
        self.fields = copy.deepcopy(sample_dict)
        self.id = sample_dict['id']
        self.title = sample_dict['title']
        self.taxon = sample_dict['taxon_id']
        del sample_dict['id']
        del sample_dict['title']
        del sample_dict['taxon_id']
        self.attributes = sample_dict
