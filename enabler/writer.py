#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
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


def project(output_dir, title, unique_name, description='short abstract'):
    """This function writes the project XML
    """
    logger = logging.getLogger(__name__)
    project_xml = template_dir + 'project.xml'

    title_string = '<TITLE>%s</TITLE>' % title
    add_title = et.fromstring(title_string)

    description_string = '<DESCRIPTION>%s</DESCRIPTION>' % description
    add_description = et.fromstring(description_string)

    tree = et.parse(project_xml)
    root = tree.getroot()

    et.SubElement(root, 'PROJECT').set('alias', unique_name)

    for project in root.iter('PROJECT'):
        project.append(add_title)
        project.append(add_description)

    tree.write(output_dir + 'project.xml')


def sample(output_dir, samples):
    """This function writes the sample xml
    """
    logger = logging.getLogger(__name__)
    sample_xml = template_dir + 'sample.xml'

    tree = et.parse(sample_xml)
    root = tree.getroot()

    # TODO parse sample cheet in sample Class

    for sample in samples:
        s = et.SubElement(root, 'SAMPLE', attrib={"alias": sample_name})
        et.SubElement(s, 'TITLE', value=title)
        n = et.SubElement(s, 'SAMPLE_NAME')
        et.SubElement(n, 'TAXDON_ID', value=taxid)

        for attribute in sample.attributes:
            pass
