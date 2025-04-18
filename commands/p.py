import subprocess
import click

@click.command(help="Push the current code to a specific branch on GitHub.")
@click.argument('branch', metavar='[BRANCH]')

def p(branch):
    """Push into your GitHub"""
    cmd = ['git', 'push', 'origin', branch]
    try:
        result = subprocess.run(cmd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro:", e.stderr)

if __name__ == "__main__":
    p()