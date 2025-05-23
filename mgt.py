#!/usr/bin/env python3

import click
from commands.run import run
from commands.c import c
from commands.p import p

@click.group()
def cli():
    """MyGit-CLI"""
    pass

cli.add_command(run)
cli.add_command(p)
cli.add_command(c)

if __name__ == '__main__':
    cli()
