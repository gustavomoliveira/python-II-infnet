from validacoes import *

def menu():
    opcao = validar_opcao(
    '\n========================\n\n'
    '--> Menu de Produtos <--\n'
    '[1] - Inserir Produto\n'
    '[2] - Consultar Produto\n'
    '[3] - Alterar Produto\n'
    '[4] - Excluir Produto\n'
    '[0] - Finalizar Menu\n'
   '\n========================\n'
    'Digite a opção desejada: '
    )
    return opcao