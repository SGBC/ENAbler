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

    action_string = f'<ACTION><{action} /></ACTION>'
    add_action = et.fromstring(action_string)

    if action == 'ADD':
        release_string = f'<ACTION><{release} /></ACTION>'
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

    title_string = f'<TITLE>{title}</TITLE>'
    add_title = et.fromstring(title_string)

    description_string = f'<DESCRIPTION>{description}</DESCRIPTION>'
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

    for sample in samples:
        s = et.SubElement(root, 'SAMPLE', attrib={"alias": sample.id})
        et.SubElement(s, 'TITLE', value=sample.title)
        n = et.SubElement(s, 'SAMPLE_NAME')
        et.SubElement(n, 'TAXDON_ID', value=sample.taxon_id)

        if sample.attributes:
            attributes = et.SubElement(s, 'SAMPLE_ATTRIBUTES')

        for tag, value in sample.attributes.items():
            attribute = et.SubElement(attributes, 'SAMPLE_ATTRIBUTE')
            et.SubElement(attribute, 'TAG', value=tag)
            et.SubElement(attribute, 'VALUE', value=value)

    tree.write(output_dir + 'sample.xml')
