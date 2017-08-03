#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ec2ips` package."""

import pytest

from click.testing import CliRunner
import os
import boto3
from ec2ips import ec2ips
from ec2ips import cli
from pprint import pprint

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

@pytest.fixture
def ec2client_mock(monkeypatch):

    class ec2client_mock(object):

        def describe_instances(self):
            if 'mock_errors' in os.environ:
                pass
            else:
                return {
                    'Reservations': [
                        { 'Instances': [
                            {
                                'State': {
                                    'Code': 16
                                },
                                'PublicIpAddress': '1.2.3.4',
                                'Tags': [
                                    { 'Key': 'Key', 'Value': 'Value' },
                                    { 'Key': 'Name', 'Value': 'Server1' }
                                ]
                            },
                            {
                                'State': {
                                    'Code': 16
                                },
                                'PublicIpAddress': '5.6.7.8',
                                'Tags': [
                                    { 'Key': 'Key', 'Value': 'Value' },
                                    { 'Key': 'Name', 'Value': 'Server2' }
                                ]

                            },
                            {
                                'State': {
                                    'Code': 16
                                },
                                'PublicIpAddress': '9.10.11.12',
                                'Tags': [
                                    { 'Key': 'Key', 'Value': 'Value' },
                                    { 'Key': 'Name', 'Value': 'Server2' }
                                ]

                            }

                        ]
                        },
                        {'Instances': [
                            {
                                'State': {
                                    'Code': 20
                                }
                            },
                            {
                                'State': {
                                    'Code': 90
                                }
                            }
                        ]
                    }]
                }
        def describe_addresses(self):
            pass

    def client_mock(arg, **kwargs):
        return ec2client_mock()

    monkeypatch.setattr(boto3, 'client', client_mock)


def test_client(ec2client_mock):

    ec2 = ec2ips.ec2client()
    pprint(ec2)

    # assert ec2 == 'ec2'

def test_ec2ips_list_names(ec2client_mock):

   servers = ec2ips.list_names()
   pprint(servers)


def __test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def __test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'ec2ips.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
