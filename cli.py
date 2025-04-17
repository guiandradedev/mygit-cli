import click
from comandos.run import run
from comandos.c import c

@click.group()
def cli():
    """Minha CLI personalizada"""
    pass

cli.add_command(run)
cli.add_command(c)

if __name__ == '__main__':
    cli()
