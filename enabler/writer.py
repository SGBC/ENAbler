#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import xml.etree.ElementTree as et


template_dir = os.path.dirname(__file__) + '/templates/'


def submission(output_dir, action='ADD', release='RELEASE', date=''):
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


def project(output_dir):
    """
    """
    pass
