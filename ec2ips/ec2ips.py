# -*- coding: utf-8 -*-

import boto3
import os

"""Main module."""

def ec2client(**kwargs):

    defs = {
            'region_name': 'us-west-2'
            }

    defs.update(kwargs)

    ec2 = boto3.client("ec2", **defs)

    return ec2


def all_ips(**kwargs):

    client_defs = {
                'region_name': get_default_region(),
            }

    client_defs.update(kwargs)

    ec2 = ec2client(**client_defs)

    i = ec2.describe_instances()

    ips = []

    for a in i['Reservations']:
        for aa in a['Instances']:
            print(aa['PublicIpAddress'])

def list_names(**kwargs):
    client_defs = {
            'region_name': get_default_region(),
            }

    client_defs.update(kwargs)

    ec2 = ec2client(**client_defs)

    i = ec2.describe_instances()

    names = {}

    for a in i['Reservations']:
        for aa in a['Instances']:
            name = False
            for tag in aa['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
            if name:
                if name in names:
                    names[name] += 1
                else:
                    names.update({name: 1})


    if len(names)>0:
        print("Name : #instances")
        for k, v in names.items():
            print('{0}: {1}'.format(k, v))

def name_equals(name, **kwargs):

    client_defs = {
            'region_name': get_default_region(),
            'contains': False
            }

    client_defs.update(kwargs)

    ec2 = ec2client(**client_defs)

    i = ec2.describe_instances()

    ips = []
    for a in i['Reservations']:
        for aa in a['Instances']:
            tag_name = False
            for tag in aa['Tags']:
                if tag['Key'] == 'Name':
                    tag_name = tag['Value']
            if client_defs['contains']:
                if name.lower() in tag_name.lower():
                    if 'PublicIpAddress' in aa:
                        print(aa['PublicIpAddress'])
            else:
                if tag_name and tag_name.lower() == name.lower():
                    if 'PublicIpAddress' in aa:
                        print(aa['PublicIpAddress'])


def get_default_region():
    if 'AWS_DEFAULT_REGION' in os.environ:
        return os.environ['AWS_DEFAULT_REGION']
    else:
        return 'us-west-2'

