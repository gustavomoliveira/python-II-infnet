from util import *
from tabulate import tabulate
from constantes import *

ID_CLIENTE = 0
TOTAL_CLIENTE = 1

def menu_caixa():
    while True:
        print('\nO que deseja fazer?')
        print('[1] - Atender Cliente')
        print('[2] - Fechar Caixa')
        opcao = entrar_inteiro('\nDigite a opção desejada: ')
        if opcao in (1, 2): # forma diferente de validação, por conjunto
            break
        else:
            print('ERRO: Opção inválida.')
    return opcao

def fechar_caixa(clientes):
    print('\nFechamento do Caixa')
    print(exibir_data() + '\n')
    total_caixa = 0
    for cliente in clientes:
        cliente[0] = str(cliente[ID_CLIENTE])
        total_caixa += cliente[TOTAL_CLIENTE]
    print(tabulate(clientes, headers=['Cliente', 'Total']))
    print('\nClientes Atendidos:', len(clientes))
    print('Total: R$', total_caixa)

def verificar_estoque(produtos):
    sem_estoque = []
    for produto in produtos:
        if produto[QTDE_PRODUTO] == 0:
            sem_estoque.append([produto[NOME_PRODUTO]])
    if sem_estoque:
        print()
        print(tabulate(sem_estoque, headers=['Produto']))
        print()