# -*- coding: utf-8 -*-

import boto3
import os
import collections

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
            if 'PrivateIpAddress' in aa:
                ips.append(aa['PrivateIpAddress'])

    return ips

def list_ips(**kwargs):
    client_defs = {
            'region_name': get_default_region(),
            }

    client_defs.update(kwargs)

    ec2 = ec2client(**client_defs)


    # get elastic IP's
    eips = []

    ips = ec2.describe_addresses()

    for a in ips['Addresses']:
        eips.append(a['PublicIp'])

    i = ec2.describe_instances()
    servers = []

    for a in i['Reservations']:
        for aa in a['Instances']:
            if aa['State']['Code'] != 16:
                continue;
            if 'PrivateIpAddress' not in aa:
                continue

            ip = aa['PrivateIpAddress']
            name = ''

            for tag in aa['Tags']:
                if tag['Key'] == 'Hostname':
                    name = tag['Value']

            line = '{0}: {1}'.format(name, ip)
            servers.append(line)

    servers = sorted(servers)

    for k, v in enumerate(servers):
        ip = v.split(':')[1].lstrip()
        pre = '  '
        if ip in eips:
            pre = '* '

        servers[k] = '{0}{1}'.format(pre,v)

    return servers

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
            if aa['State']['Code'] != 16:
                continue;
            name = False
            for tag in aa['Tags']:
                if tag['Key'] == 'Hostname':
                    name = tag['Value']
            if name:
                if name in names:
                    names[name] += 1
                else:
                    names.update({name: 1})

    servers = []

    for k, v in names.items():
        servers.append('{0}: {1}'.format(v, k))

    return servers


def name_equals(name, **kwargs):

    contains = False

    if 'contains' in kwargs:
        contains = kwargs['contains']

    client_defs = {
            'region_name': get_default_region(),
            }

    client_defs.update(kwargs)

    if 'contains' in client_defs:
        del client_defs['contains']

    ec2 = ec2client(**client_defs)

    i = ec2.describe_instances()

    ips = []
    for a in i['Reservations']:
        for aa in a['Instances']:
            if aa['State']['Code'] != 16:
                continue;
            tag_name = False
            for tag in aa['Tags']:
                if tag['Key'] == 'Hostname':
                    tag_name = tag['Value']
            if contains:
                if name.lower() in tag_name.lower():
                    if 'PrivateIpAddress' in aa:
                        print(aa['PrivateIpAddress'])
            else:
                if tag_name and tag_name.lower() == name.lower():
                    if 'PrivateIpAddress' in aa:
                        print(aa['PrivateIpAddress'])


def get_default_region():
    if 'AWS_DEFAULT_REGION' in os.environ:
        return os.environ['AWS_DEFAULT_REGION']
    else:
        return 'us-west-2'

