from CRUD_BD.crud_produto_bd import *

def consultar_produto(id_produto):
    produto = consultar_produto_bd(id_produto)
    if not produto:
        print('\nProduto não encontrado no sistema.')
        return False
    else:
        return produto
        
def consultar_produto_nome(nome_produto):
    novo_produto = consultar_produto_nome_bd(nome_produto)
    if not novo_produto:
        print('\nProduto não encontrado no sistema.')
        return False
    else:
        return novo_produto
    
def consultar_todos_produtos():
    produtos = consultar_todos_produtos_bd()
    if not produtos:
        print('\nProdutos não encontrados no sistema.')
        return False
    else:
        return produtos
    
def consultar_tamanho_produtos():
    resultado = consultar_tamanho_produtos_bd()
    if resultado is None:
        return False
    else:
        return resultado
    
def incluir_produto(nome, quantidade, preco):
    sucesso = incluir_produto_bd(nome, quantidade, preco)
    if sucesso:
        print(f'\nO novo item "{nome}" foi inserido com sucesso no sistema.')

def atualizar_produto(produto):
    sucesso = atualizar_produto_bd(produto)
    if sucesso:
        print(f'\nProduto atualizado com sucesso.')

def consultar_estoque_final():
    produtos = consultar_todos_produtos_bd()
    if not produtos:
        print('\nNão foi possível consultar o estoque no sistema.')
        return False
    else:
        estoque = [[produto[1], produto[2]] for produto in produtos]
        return estoque
    
def atualizar_todo_estoque(produtos):
    sucesso = atualizar_todo_estoque_bd(produtos)
    if sucesso:
        print(f'\nEstoque de produtos atualizado com sucesso!')
    return sucesso