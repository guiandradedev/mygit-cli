import click
import subprocess
import inquirer

@click.command()
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
def c(args):
    commit_emojis = {
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
    # Criar uma lista de opções para o `inquirer`
    options = [f"{tipo} {emoji}" for tipo, emoji in commit_emojis.items()]

    # Perguntar ao usuário qual o tipo de commit usar
    questions = [
        inquirer.List('commit_type',
                      message="Escolha o tipo de commit",
                      choices=options,
                      carousel=True)
    ]

    # Captura a resposta
    answers = inquirer.prompt(questions)
    tipo = None
    emoji = None

    if answers:
        # Extraímos o tipo e emoji escolhido
        commit_choice = answers['commit_type'].split(" ", 1)
        tipo, emoji = commit_choice[0], commit_choice[1]
        print(f"Você escolheu: {tipo} {emoji}")
    else:
        print("Nenhuma escolha feita.")

    mensagem = input("Insira a mensagem: ")

    cmd = f"git commit -m {emoji} {tipo}: {mensagem}"
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro:", e.stderr)    

    # Aqui você pode continuar para capturar a mensagem do commit ou outros passos
    # commit_message = input("Qual a mensagem do commit?")
    # print(f"Commit realizado: {emoji} {tipo}: {commit_message}")

if __name__ == "__main__":
    c()
