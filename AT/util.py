from validacoes import *
from crud_db import *

def validar_disponibilidade_produto(produtos):
    while True:
        id = validar_inteiro('\nInsira o ID do produto para consultar sua disponibilidade em estoque: ')
        for produto in produtos:
            estoque_disponivel = produto[2] if len(produto) == 4 else produto[4]
            if id == produto[0]:
                if estoque_disponivel > 0:
                    print(f'\n{produto[1]} encontrado! Quantidade: {estoque_disponivel} | Preço: R$ {produto[3]}.')
                    print(produto)
                    return produto

                print(f'\n{produto[1]} encontrado, porém não existe estoque disponível no momento.')
                return
            
        print('\nProduto não encontrado.')
        opcao = validar_escolha('\nDeseja cadastrar o produto no sistema? ([1] - Sim / [2] - Não): ')
        if opcao == 2:
            print('\nEncerrando o cadastro de um novo produto.')
            return

        nome = validar_nome('\nInsira o nome do produto a ser cadastrado: ')
        quantidade = validar_quantidade('\nInsira a quantidade do produto a ser cadastrado: ')
        preco = validar_preco('\nInsira o preço do produto a ser cadastrado: ')

        novo_produto = (len(produtos) + 1, nome, quantidade, preco)
        print(f'\nProduto "{nome}" cadastrado com sucesso! Quantidade: {quantidade} | Preço: R$ {preco:.1f}')
        return novo_produto