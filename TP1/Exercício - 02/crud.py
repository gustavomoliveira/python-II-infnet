from validacoes import *
from utilitario import *

def inserir_funcionario(projeto_1, projeto_2):
    print(f'\nProjetos disponíveis para inserir funcionários:')
    print('\nProjeto 1')
    exibir_funcionarios(projeto_1)
    print('\nProjeto 2')
    exibir_funcionarios(projeto_2)
    escolha = validar_projeto('\nEm qual projeto deseja adicionar um funcionário? Digite [1] ou [2]: ')
    projeto = escolher_projeto(escolha, projeto_1, projeto_2)
    funcionario = validar_nome('\nDigite o nome do funcionário a ser adicionado: ')
    if funcionario in projeto:
        print(f'\nJá existe um funcionário com o nome {funcionario} e o Projeto {escolha} não aceita funcionários com o mesmo nome.')
        projeto.add(funcionario)
        exibir_funcionarios(projeto)
    else:
        projeto.add(funcionario)
        print(f'\nFuncionário adicionado com sucesso.')

def verificar_duplicatas(projeto_1, projeto_2):
    escolha = validar_projeto('\nQual projeto gostaria de verificar? Digite [1] ou [2]: ')
    print(f'\nO Projeto {escolha} possui os seguintes funcionários: ')
    projeto = escolher_projeto(escolha, projeto_1, projeto_2)
    exibir_funcionarios(projeto)
    print(f'\nEstes são os funcionários que desejam entrar no Projeto {escolha}: ')

    if escolha == 1:
        novos_funcionarios = ['F1', 'F2', 'F3', 'F4', 'F999']
    else:
        novos_funcionarios = ['F1', 'F5', 'F3', 'F6', 'F998']

    for funcionario in novos_funcionarios:
        print(funcionario)
        projeto.add(funcionario)

    print(f'\nExistem vários de mesmo nome, mas o Projeto {escolha} aceitou apenas aquele de nome diferente, o {novos_funcionarios[-1]}: ')
    exibir_funcionarios(projeto)
    print('\nIsso prova que não é possível existir funcionários repetidos, de mesmo nome, em um mesmo projeto.')
    
    if escolha == 1:
        projeto.remove('F999')
    else:
        projeto.remove('F998')

def excluir_funcionario(projeto_1, projeto_2):
    escolha = validar_projeto('\nDe qual projeto gostaria de excluir um funcionário? Digite [1] ou [2]: ')
    print(f'\nO Projeto {escolha} possui os seguintes funcionários: ')
    projeto = escolher_projeto(escolha, projeto_1, projeto_2)
    exibir_funcionarios(projeto)
    nome = validar_nome(f'\nDigite o nome do funcionário que deseja excluir do Projeto {escolha}: ')
    if nome in projeto or nome in ('F999', 'F998'):
        projeto.remove(nome)
        print(f'\nFuncionário {nome} removido com sucesso.')
    else:
        print(f'\nERRO: Funcionário {nome} não está presente no projeto.')