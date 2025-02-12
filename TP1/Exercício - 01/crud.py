from tabulate import tabulate
from validacoes import *

def inserir_produto(produtos):
    chave = validar_chave('\nDigite um número inteiro para a Chave: ')
    if chave not in produtos:
        nome = input('\nDigite o nome do Produto: ').title()
        quantidade = validar_quantidade('\nDigite a quantidade do Produto: ')
        preco = validar_preco('\nDigite o preço do Produto: ')
        produtos[chave] = [nome, quantidade, preco]
        print(f'\nO produto -> {produtos[chave][0]} <- foi inserido com sucesso!')
    else:
        print(f'\nERRO: Chave {chave} já existe.')
    return produtos

def consultar_produto(produtos):
    chave = validar_chave('\nDigite a Chave do produto para realizar a consulta: ')
    if chave in produtos:
        print(f'\nProduto encontrado: Nome - {produtos[chave][0]} | Qtde - {produtos[chave][1]} | Preço - {produtos[chave][2]}')
    else:
        print(f'\nNão existe um produto cadastrado com a chave: {chave}.')

def alterar_produto(produtos):
    chave = validar_chave('\nDigite a Chave do produto para realizar a alteração: ')
    if chave in produtos:
        print(f'\nProduto -> {produtos[chave][0]} <- selecionado.')
        quantidade = validar_quantidade('\nDigite a nova quantidade do Produto: ')
        preco = validar_preco('\nDigite o novo preço do Produto: ')
        produtos[chave][1] = quantidade
        produtos[chave][2] = preco
        print(f'\nProduto -> {produtos[chave][0]} <- atualizado com sucesso! Nova quantidade: {produtos[chave][1]} | Novo preço: {produtos[chave][2]}.')
    else:
        print(f'\nNão existe um produto cadastrado com a chave: {chave}.')
    return produtos

def excluir_produto(produtos):
    chave = validar_chave('\nDigite a Chave do produto para realizar a exclusão: ')
    if chave in produtos:
        print(f'\nO produto -> {produtos[chave][0]} <- foi removido com sucesso.')
        produtos.pop(chave)
    else:
        print(f'\nNão existe um produto cadastrado com a chave: {chave}.')

def exibir_produtos(produtos):
    if produtos:
        print()
        print(tabulate(produtos.values(), headers=['Nome', 'Qtde', 'Preço'], stralign='center', numalign='center', tablefmt='rounded_outline'))
    else:
        print(f'\nNão há produtos cadastrados para serem exibidos.\n')