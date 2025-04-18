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
@click.option('--type', '-t', help='Tipo do commit (ex: feat, fix, chore, etc)')
@click.option('--message', '-m', help='Mensagem do commit')
@click.option('--dry', is_flag=True, help='Somente exibe o comando sem executar')
@click.option('--content', '-c', multiple=True, help="Conteúdo que vai pro commit")
def c(type, message, dry, content):
    if not type:
        options = [f"{emoji} {tipo}" for tipo, emoji in COMMIT_TYPES.items()]
        answer = inquirer.prompt([
            inquirer.List("commit_type", message="Escolha o tipo de commit", choices=options)
        ])
        if answer:
            type = answer["commit_type"].split()[1]  # pegando "tipo" no final
        else:
            click.echo("❌ Nenhuma opção selecionada.")
            return

    if type not in COMMIT_TYPES:
        click.echo(f"❌ Tipo '{type}' inválido. Use um dos seguintes: {', '.join(COMMIT_TYPES.keys())}")
        return

    if not message:
        message = input("📝 Insira a mensagem de commit: ")

    emoji = COMMIT_TYPES[type]
    full_message = f'{emoji} {type}: {message}'

    # Adicionando arquivos
    cmd_add = ["git", "add", *content] if content else None
    if not cmd_add:
        confirm = inquirer.prompt([
            inquirer.Confirm('add_all', message='Nenhum conteúdo especificado. Adicionar tudo com "git add ."?', default=False)
        ])
        if confirm and confirm["add_all"]:
            cmd_add = ["git", "add", "."]
        else:
            click.echo("❌ Nenhum arquivo adicionado. Commit cancelado.")
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
            click.echo("✅ Commit realizado com sucesso:")
            click.echo(full_message)
            click.echo(result.stdout)
        except subprocess.CalledProcessError as e:
            click.echo(f"❌ Erro ao executar git: {e.stderr}")

if __name__ == "__main__":
    c()