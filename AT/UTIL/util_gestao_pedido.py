from UTIL.util_entrada import *
from UTIL.util_gestao_produto import adicionar_um_produto, atualizar_produto
from CRUD.crud_item import incluir_item

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

def ajustar_produto_com_estoque_temporario(produto, estoque_temporario):
    id_produto = produto[0]
    estoque_real = produto[2]
    
    if id_produto in estoque_temporario:
        estoque_disponivel = estoque_real - estoque_temporario[id_produto]
        
        if estoque_disponivel <= 0:
            print(f'\n{produto[1]} já adicionado ao carrinho e sem estoque adicional disponível.')
            return None
            
        if len(produto) >= 5:
            return (produto[0], produto[1], estoque_disponivel, produto[3], produto[4])
        else:
            return (produto[0], produto[1], estoque_disponivel, produto[3], estoque_disponivel)
        
    return produto

def continuar_adicionando_produtos():
    opcao = validar_escolha('\nDeseja adicionar mais produtos ao pedido? ([1] - Sim / [2] - Finalizar Atendimento): ')
    if opcao == 2:
        print('\nInserção de produtos finalizada.')
        return False
    
    return True

def organizar_produtos(produtos_pedido, compra_atual):
    for produto in produtos_pedido:
        nome_produto = produto[1]
        quantidade_escolhida = produto[2]
        
        print(f'\nAtualizando produto: {nome_produto}')
        atualizar_produto(produto)
        incluir_item(quantidade_escolhida, compra_atual, produto)