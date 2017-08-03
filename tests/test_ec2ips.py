#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ec2ips` package."""

import pytest

from click.testing import CliRunner

from ec2ips import ec2ips
from ec2ips import cli
import boto3
from pprint import pprint

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

@pytest.fixture
def scaffold_boto3(monkeypatch):

    def boto3_client(arg, **kwargs):
        return [arg, kwargs]

    monkeypatch.setattr(boto3, 'client', boto3_client)


def test_client(scaffold_boto3):

    ec2 = ec2ips.ec2client()
    pprint(ec2)

    # assert ec2 == 'ec2'





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
