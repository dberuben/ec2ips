# -*- coding: utf-8 -*-

"""Console script for ec2ips."""

import click
import ec2ips

@click.group()
def main(args=None):
    """Console script for ec2ips."""
    pass


@main.command()
@click.option('--region',default=None,help='Region to use. Default: us-west-2 or env[AWS_DEFAULT_REGION]')
def all(region):
    ips = ec2ips.all_ips(region_name=region)

    if len(ips)<=0:
        click.echo("No ips")
        return

    for ip in ips:
        click.echo(ip)


@main.command(help='return ips by instance name. use --contains flag for fuzzy search. *not case sensitive')
@click.argument('name')
@click.option('--region',default=None,help='Region to use. Default: us-west-2 or env[AWS_DEFAULT_REGION]')
@click.option('--contains',is_flag=True,default=False,help='flag to use fuzzy search')
def name(name,region,contains):
    ec2ips.name_equals(name,region_name=region,contains=contains)

@main.command(help='List all instance name tags for referenc')
@click.option('--region',default=None,help='Region to use. Default: us-west-2 or env[AWS_DEFAULT_REGION]')
def list_names(region):
    servers = ec2ips.list_names(region_name=region)
    if len(servers)<=0:
        click.echo("No servers available")
        return

    click.echo("--------------")
    click.echo("#instances : Name")
    click.echo("--------------")
    for s in servers:
        click.echo(s)

@main.command(help='List all instances w/ips for reference')
@click.option('--region',default=None,help='Region to use. Default: us-west-2 or env[AWS_DEFAULT_REGION]')
def list_ips(region):
    servers = ec2ips.list_ips(region_name=region)
    if len(servers)<=0:
        click.echo("No servers available")
        return

    click.echo("--------------")
    click.echo("* denotes server with dedicated EIP")
    click.echo("--------------")
    for s in servers:
        click.echo(s)

if __name__ == "__main__":
    main()
