#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse

from enabler.upload import upload
from enabler.submit import submit


def main():
    parser = argparse.ArgumentParser(
        prog='enabler',
        usage='enabler <command> [options]',
        description='programmatic ENA submission'
    )
    subparsers = parser.add_subparsers(
        title='available subcommands',
        metavar=''
    )

    parser_upload = subparsers.add_parser(
        'upload',
        prog='enabler upload',
        description='upload data to ENA',
        help='upload data to ENA'
    )
    param_logging_u = parser_upload.add_mutually_exclusive_group()
    param_logging_u.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        default=False,
        help=f'disable info logging. (default: {default}).'
    )
    param_logging_u.add_argument(
        '--debug',
        '-d',
        action='store_true',
        default=False,
        help=f'enable debug logging. (default: {default}).'
    )
    parser_upload.add_argument(
        '--input',
        '-i',
        metavar='',
        required=True,
        help='input directory'
    )
    parser_upload._optionals.title = 'arguments'
    parser_upload.set_defaults(func=upload)

    parser_submit = subparsers.add_parser(
        'submit',
        prog='enabler submit',
        description='submit to ENA',
        help='submit to ENA'
    )
    param_logging_s = parser_submit.add_mutually_exclusive_group()
    param_logging_s.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        default=False,
        help=f'disable info logging. (default: {default}).'
    )
    param_logging_s.add_argument(
        '--debug',
        '-d',
        action='store_true',
        default=False,
        help=f'enable debug logging. (default: {default}).'
    )
    parser_submit.add_argument(
        '--username',
        '-u',
        help='Your webin username'
    )
    parser_submit.add_argument(
        '--action',
        '-a',
        choices=['add', 'modify', 'release', 'validate'],
        default='add',
        help=f'action to perform. (default: {default}).'
    )
    parser_submit.add_argument(
        '--title',
        '-t',
        help='title of your study',
        required=True
    )
    parser_submit.add_argument(
        '--name',
        '-n',
        help='Unique name for your study. Will be a random string of 5 \
            characters if not specified.',
    )
    parser_submit.add_argument(
        '--samples',
        '-s',
        help='sample information in tabular or csv format'
    )
    parser_submit.add_argument(
        '--output',
        '-o',
        required=True,
        help='output directory where to store the XML used for submission'
    )
    parser_submit._optionals.title = 'arguments'
    parser_submit.set_defaults(func=submit)

    args = parser.parse_args()

    # set logger
    try:
        if args.quiet:
            logging.basicConfig(level=logging.ERROR)
        elif args.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

        args.func(args)
    except AttributeError as e:
        logger = logging.getLogger(__name__)
        logger.debug(e)
        parser.print_help()
