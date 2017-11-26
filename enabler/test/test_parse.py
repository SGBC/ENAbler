#!/usr/bin/env python

from enabler import parse


def test_is_gzipped():
    gzipped_file = 'data/ecoli_R1.fastq.gz'
    not_gzipped_file = 'data/a_nonempty_file'
    assert parse.is_gzipped(gzipped_file) is True
    assert parse.is_gzipped(not_gzipped_file) is False


def test_calc_md5():
    gzipped_file = 'data/ecoli_R1.fastq.gz'
    md5 = parse.calc_md5(gzipped_file)
    assert md5 == 'd7e4bdf56d258837ca3b234fbba63620'


def test_md5_to_file():
    gzipped_file = 'data/ecoli_R1.fastq.gz'
    md5 = parse.calc_md5(gzipped_file)
    parse.md5_to_file(gzipped_file, md5)

    with open(gzipped_file + '.md5') as f:
        lm = f.readlines()
        assert lm == ['d7e4bdf56d258837ca3b234fbba63620  ecoli_R1.fastq.gz\n']
