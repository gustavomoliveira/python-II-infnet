from UTIL.util_entrada import *
from UTIL.util_gestao_produto import adicionar_um_produto, atualizar_todo_estoque
from CRUD.crud_item import incluir_item

def adicionar_produtos_pedido(cliente):
    produtos_pedido = []
    estoque_temporario = {}

    while True:
        produto_adicionado = adicionar_um_produto(cliente, estoque_temporario)
        
        if produto_adicionado:
            produtos_pedido.append(produto_adicionado)
        
        if not continuar_adicionando_produtos():
            break
            
    return produtos_pedido

def solicitar_quantidade(produto):
    quantidade = validar_inteiro(f'\nDigite a quantidade do {produto[1]} desejada: ')
    
    estoque_disponivel = produto[2]
    
    if quantidade > estoque_disponivel:
        print(f'\nQuantidade selecionada é maior que o estoque disponível.')
        print(f'\nQuantidade disponível: {estoque_disponivel}')
        return None, estoque_disponivel
    
    estoque_restante = estoque_disponivel - quantidade
    return quantidade, estoque_restante

def atualizar_estoque_temporario(id_produto, quantidade, estoque_temporario):
    if id_produto in estoque_temporario:
        estoque_temporario[id_produto] += quantidade
    else:
        estoque_temporario[id_produto] = quantidade

def continuar_adicionando_produtos():
    opcao = validar_escolha('\nDeseja adicionar mais produtos ao pedido? ([1] - Sim / [2] - Finalizar Atendimento): ')
    if opcao == 2:
        print('\nInserção de produtos finalizada.')
        return False
    return True

def organizar_produtos(produtos_pedido, compra_atual):
    for produto in produtos_pedido:
        quantidade_escolhida = produto[2]
        incluir_item(quantidade_escolhida, compra_atual, produto)
    
    atualizar_todo_estoque(produtos_pedido)