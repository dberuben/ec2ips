# -*- coding: utf-8 -*-

import boto3

"""Main module."""

def ec2client(**kwargs):

    if 'region' in kwargs:
        region=kwargs['region']
    else:
        region='us-west-2'

    ec2 = boto3.client("ec2", region_name=region)

    return ec2


def all_ips(**kwargs):

    client_defs = {
                'region_name': 'us-east-1'
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
            'region_name': 'us-west-2'
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
                names.update({name: name})


    if len(names)>0:
        for name in names:
            print(name)

def name_equals(name, **kwargs):

    client_defs = {
            'region_name': 'us-east-1',
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
