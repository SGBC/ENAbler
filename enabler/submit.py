#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

import xml.etree.ElementTree as et


template_dir = os.path.dirname(__file__) + '/templates/'


def submit(args):
    """Main function for the `enabler submit` command
    """
    logger = logging.getLogger(__name__)
    logger.debug('Using verbose logger')
    # logger.error('This function is not available yet')

    action = args.action.upper()
    write_submission_xml(args.output, action)


def write_submission_xml(output_dir, action='ADD', release='RELEASE', date=''):
    """This function writes the submission XML
    """
    logger = logging.getLogger(__name__)
    submission_xml = template_dir + 'submission.xml'

    action_string = '<ACTION><%s /></ACTION>' % action
    add_action = et.fromstring(action_string)

    if action == 'ADD':
        release_string = '<ACTION><%s /></ACTION>' % release
        add_release = et.fromstring(release_string)

    tree = et.parse(submission_xml)
    root = tree.getroot()

    for actions in root.iter('ACTIONS'):
        actions.append(add_action)
        if action == 'ADD':
            actions.append(add_release)

    tree.write(output_dir + 'submission.xml')
