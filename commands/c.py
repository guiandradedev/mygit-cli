import click
import subprocess
import inquirer

COMMIT_TYPES = {
    "feat": "✨",         # uma nova feature
    "fix": "🐛",          # correção de bug
    "docs": "📝",         # documentação
    "style": "💄",        # estilos (formatação, ponto e vírgula, etc)
    "refactor": "♻️",     # refatoração de código
    "perf": "⚡️",         # melhorias de performance
    "test": "✅",         # testes
    "build": "👷",        # mudanças de build ou dependências
    "ci": "🔧",           # mudanças de CI (integração contínua)
    "chore": "🔨",        # tarefas diversas
    "revert": "⏪️",      # reverter commit
    "release": "🚀",      # nova versão
    "deploy": "🚀",       # deploy (pode ser igual ao release)
    "init": "🎉",         # commit inicial
    "merge": "🔀",        # merge de branches
    "config": "⚙️",       # configuração
    "hotfix": "🚑️",      # correção urgente
    "security": "🔒️",    # correção de vulnerabilidades
    "remove": "🔥",       # remoção de código ou arquivos
    "add": "➕",          # adição de arquivos
    "update": "⬆️",      # atualização de código, dependências, etc
    "downgrade": "⬇️",   # downgrade de dependências
    "move": "🚚",         # mover/renomear arquivos
    "rename": "✏️",      # renomear arquivos
}
@click.command()
@click.option('--type', '-t', help='Type of commit (e.g., feat, fix, chore, etc)')
@click.option('--message', '-m', help='Commit message')
@click.option('--dry', is_flag=True, help='Only display the command without executing it')
@click.option('--content', '-c', multiple=True, help="Content to include in the commit")
def c(type, message, dry, content):
    """Commit into your GitHub"""
    if not type:
        options = [f"{emoji} {tipo}" for tipo, emoji in COMMIT_TYPES.items()]
        answer = inquirer.prompt([
            inquirer.List("commit_type", message="Choose the type of commit", choices=options)
        ])
        if answer:
            type = answer["commit_type"].split()[1]  # extracting "type" at the end
        else:
            click.echo("❌ No option selected.")
            return

    if type not in COMMIT_TYPES:
        click.echo(f"❌ Invalid type '{type}'. Use one of the following: {', '.join(COMMIT_TYPES.keys())}")
        return

    if not message:
        message = input("📝 Enter the commit message: ")

    emoji = COMMIT_TYPES[type]
    full_message = f'{emoji} {type}: {message}'

    # Adding files
    cmd_add = ["git", "add", *content] if content else None
    if not cmd_add:
        confirm = inquirer.prompt([
            inquirer.Confirm('add_all', message='No content specified. Add everything with "git add ."?', default=False)
        ])
        if confirm and confirm["add_all"]:
            cmd_add = ["git", "add", "."]
        else:
            click.echo("❌ No files added. Commit canceled.")
            return

    cmd_commit = ["git", "commit", "-m", full_message]

    if dry:
        subprocess.run("git status", shell=True)
        click.echo(f"[dry-run] {' '.join(cmd_add)}")
        click.echo(f"[dry-run] {' '.join(cmd_commit)}")
    else:
        try:
            subprocess.run(cmd_add, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = subprocess.run(cmd_commit, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            click.echo("✅ Commit successfully made:")
            click.echo(full_message)
            click.echo(result.stdout)
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ Error executing git: {e.stderr}")

if __name__ == "__main__":
    c()