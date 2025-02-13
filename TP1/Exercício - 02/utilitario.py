from principal import iniciar_programa
from validacoes import *

def menu_principal():
    opcao = validar_opcao(
    '\n========================\n\n'
    '--> Gestão de Projetos e Funcionários <--\n\n'
    '[1] - Inserir Funcionário\n'
    '[2] - Verificar Duplicatas\n'
    '[3] - Submenu de Projetos e Funcionários\n'
    '[4] - Excluir funcionário\n'
    '[0] - Finalizar\n'
   '\n========================\n'
    'Digite a opção desejada: '
    )
    return opcao

def submenu_projetos():
    opcao = validar_opcao(
    '\n========================\n\n'
    '--> Consultas de Projetos <--\n\n'
    '[1] - Consultar Funcionários de um Projeto\n'
    '[2] - Consultar todos os Funcionários\n'
    '[3] - Consultar Funcionários presentes em ambos os Projetos\n'
    '[4] - Consultar Funcionários presentes em apenas um Projeto\n'
    '[0] - Voltar\n'
   '\n========================\n'
    'Digite a opção desejada: '
    )
    return opcao

def executar_submenu(projeto_1, projeto_2):
    while True:
        opcao = submenu_projetos()
        match opcao:
            case 1:
                consultar_funcionarios(projeto_1, projeto_2)
            case 2:
                consultar_todos(projeto_1, projeto_2)
            case 3:
                consultar_intercessao(projeto_1, projeto_2)
            case 4:
                consultar_diferenca(projeto_1, projeto_2)
            case 0:
                return
            case _:
                print('\nERRO: Opção inválida.')        

def exibir_funcionarios(projeto):
    for funcionario in projeto:
        print(funcionario)

def escolher_projeto(escolha, projeto_1, projeto_2):
    if escolha == 1:
        return projeto_1
    else:
        return projeto_2

def consultar_funcionarios(projeto_1, projeto_2):
    escolha = validar_projeto('\nEm qual projeto deseja consultar os funcionários? Digite [1] ou [2]: ')
    projeto = escolher_projeto(escolha, projeto_1, projeto_2)
    if projeto:
        print(f'\nEstes são os funcionários do Projeto {escolha}, listados em ordem crescente: ')
        print(sorted(projeto))
        print('\nMas quando exibidos, podem aparecer em uma ordem diferente da inicial, de forma aleatória:')
        print(projeto)
        print('\nApesar de serem os mesmos funcionários, nem sempre eles aparecem na mesma ordem.')
    else:
        print(f'\nO Projeto {escolha} não consta com funcionários atualmente.')

def consultar_todos(projeto1, projeto2):
    if projeto1 and projeto2:
        print(f'\nEstes são os funcionários alocados em ambos os projeto: {projeto1 | projeto2}.')
    else:
        print('\nOs projetos não contam com funcionários atualmente.')

def consultar_intercessao(projeto1, projeto2):
    if projeto1 and projeto2:
        print(f'\nEstes são os funcionários alocados nos dois projeto: {projeto1 & projeto2}.')
    else:
        print('\nOs projetos não contam com funcionários atualmente.')

def consultar_diferenca(projeto1, projeto2):
    if projeto1 and projeto2:
        print(f'\nEstes são os funcionários presentes no Projeto 1 que não estão presentes no Projeto 2: {projeto1 - projeto2}.')
        print(f'\nEstes são os funcionários presentes no Projeto 2 que não estão presentes no Projeto 1: {projeto2 - projeto1}.')
    else:
        print('\nOs projetos não contam com funcionários atualmente.')