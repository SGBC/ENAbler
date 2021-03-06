#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import getpass
import requests

from enabler.writer import submission


# test_service = 'https://www-test.ebi.ac.uk/ena/submit/drop-box/submit/'
test_service = 'https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit'
prod_service = ''


def submit(args):
    """Main function for the `enabler submit` command
    """
    logger = logging.getLogger(__name__)
    logger.debug('Using verbose logger')
    # logger.error('This function is not available yet')

    action = args.action.upper()
    # write_submission_xml(args.output, action)

    # xml file dict
    files = {
        'SUBMISSION': open(f'{args.output}/submission.xml'),
        'PROJECT': open(f'{args.output}/project.xml'),
        'SAMPLE': open(f'{args.output}/sample.xml')
    }

    # authentification
    user = args.username if args.username else input('Username: ')
    password = getpass.getpass(prompt=f'Password for {user}: ')

    r = requests.post(test_service, auth=(user, password), files=files)
    print(r.text)
