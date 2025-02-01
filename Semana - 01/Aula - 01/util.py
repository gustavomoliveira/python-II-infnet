from datetime import datetime
from constantes import *

def entrar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except:
            print('ERRO: Valor inválido.')
    return num

def pesquisar_produto(produtos, id):
    for produto in produtos:
        if produto[ID_PRODUTO] == id:
            return produto
    return None

def entrar_produto(produtos):
    while True:
        id = entrar_inteiro('Entrar com id do produto: ')
        produto = pesquisar_produto(produtos, id)
        if produto:
            break
        else:
            print('ERRO: Produto não existe.')
    return produto

def entrar_quantidade(produto):
    while True:
        quantidade = entrar_inteiro('Entrar com a quantidade: ')
        if quantidade > 0:
            if verificar_estoque(produto, quantidade):
                break
        else:
            print('ERRO: Quantidade inválida.')
    return quantidade

def verificar_estoque(produto, quantidade):
    if produto[QTDE_PRODUTO] >= quantidade:
        return True
    else:
        print('ERRO: Produto não disponível em estoque.')

def exibir_data():
    return datetime.now().strftime('%d/%m/%Y %H:%M')