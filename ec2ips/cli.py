# -*- coding: utf-8 -*-

"""Console script for ec2ips."""

import click
import ec2ips

@click.group()
def main(args=None):
    """Console script for ec2ips."""
    pass


@main.command()
@click.option('--region',default='us-west-2',help='Region to use. Default: us-west-2')
def all(region):
    ips = ec2ips.all_ips(region=region)


@main.command(help='return ips by instance name. use --contains flag for fuzzy search. *not case sensitive')
@click.argument('name')
@click.option('--region',default='us-west-2',help='Region to use. Default: us-west-2')
@click.option('--contains',is_flag=True,default=False,help='flag to use fuzzy search')
def name(name,region,contains):
    ec2ips.name_equals(name,region=region,contains=contains)

@main.command(help='List all instance name tags for referenc')
@click.option('--region',default='us-west-2',help='Region to use. Default: us-west-2')
def list_names(region):
    ec2ips.list_names(region=region)

if __name__ == "__main__":
    main()
