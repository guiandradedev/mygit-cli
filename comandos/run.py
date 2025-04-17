import click
import subprocess

@click.command()
@click.argument('cmd')
def run(cmd):
    """Executa um comando no terminal"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro:", e.stderr)
