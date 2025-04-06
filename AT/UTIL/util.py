from datetime import datetime
from UTIL.util_entrada import validar_opcao

def menu():
    opcao = validar_opcao(
        '\n=========== Caixa Supermercado ===========\n\n'
        '[1] - Iniciar Atendimento\n'
        '[2] - Exibir Estoque\n'
        '[0] - Fechar Caixa\n'
        '\n===========================================\n'
        '\nEscolha uma opção para iniciar: '
    )
    return opcao
      
def validar_data_hora():
    data_hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')
    return data_hora_atual
