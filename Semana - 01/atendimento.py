from constantes import *
from util import *
from tabulate import tabulate

def menu_atendimento():
    print('Deseja adicionar um produto?')
    print('[1] - Sim')
    print('[2] - Não')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def atender_cliente(produtos):
    itens = []
    num_item = 0
    total_compra = 0
    opcao = menu_atendimento()
    while(opcao == ADICIONAR_PRODUTO):
        num_item += 1
        produto = entrar_produto(produtos)
        quantidade = entrar_quantidade()
        total_item = quantidade * produto[PRECO_PRODUTO]
        produto[QTDE_PRODUTO] -= quantidade
        itens.append([num_item, produto[NOME_PRODUTO], quantidade, produto[PRECO_PRODUTO], total_item])
        total_compra += total_item
        opcao = menu_atendimento()
    return itens, total_compra

def fechar_atendimento(cliente, itens, total_compra):
    print('\nCliente', cliente)
    print(exibir_data() + '\n')
    print(tabulate(itens, headers=['Item', 'Produto', 'Quant.', 'Preço', 'Total']))
    print('Itens: ', len(itens))
    print('Total: R$', total_compra)