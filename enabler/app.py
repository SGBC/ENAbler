#!/usr/bin/env python

import logging
import argparse

from enabler.upload import upload


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
    param_logging = parser_upload.add_mutually_exclusive_group()
    param_logging.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        default=False,
        help='disable info logging. (default: %(default)s).'
    )
    param_logging.add_argument(
        '--debug',
        '-d',
        action='store_true',
        default=False,
        help='enable debug logging. (default: %(default)s).'
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
