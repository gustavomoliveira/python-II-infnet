from CRUD.crud_produto import *
from UTIL.util_entrada import *

def obter_produto(cliente, estoque_temporario):
    print(f'\nQual produto deseja adicionar ao pedido do {cliente[1]}?')
    id_produto = validar_inteiro('\nInsira o ID do produto para consultar sua disponibilidade em estoque: ')
    produto_bd = consultar_produto(id_produto)
    
    if not produto_bd:
        return processar_produto_inexistente()
    
    if produto_bd[2] <= 0:
        print(f'\n{produto_bd[1]} encontrado, mas sem estoque disponível.')
        return None
    
    produto = (produto_bd[0], produto_bd[1], produto_bd[2], produto_bd[3], produto_bd[2])
    
    produto_ajustado = verificar_estoque_temporario(produto, estoque_temporario)
    if not produto_ajustado:
        return None
    
    print(f'\n{produto_ajustado[1]} encontrado! Quantidade disponível: {produto_ajustado[2]} | Preço: R$ {produto_ajustado[3]}')
    
    return produto_ajustado

def verificar_estoque_temporario(produto, estoque_temporario):
    id_produto = produto[0]
    estoque_real = produto[2]
    
    if id_produto in estoque_temporario:
        estoque_disponivel = estoque_real - estoque_temporario[id_produto]
        
        if estoque_disponivel <= 0:
            print(f'\n{produto[1]} já adicionado ao carrinho e sem estoque adicional disponível.')
            return None
            
        return (produto[0], produto[1], estoque_disponivel, produto[3], produto[4])
    
    return produto

def processar_produto_inexistente():
    opcao = validar_escolha('\nDeseja cadastrar um novo produto? ([1] - Sim / [2] - Não): ')
    if opcao == 2:
        print('\nCadastro cancelado.')
        return None
    return criar_novo_produto()

def criar_novo_produto():
    nome = validar_nome('\nInsira o nome do produto a ser cadastrado: ')
    quantidade = validar_quantidade('\nInsira a quantidade do produto a ser cadastrado: ')
    preco = validar_preco('\nInsira o preço do produto a ser cadastrado: ')

    incluir_produto(nome, quantidade, preco)
    produto_cadastrado = consultar_produto_nome_bd(nome)

    print(f'\nProduto "{produto_cadastrado[1]}" cadastrado com sucesso! Quantidade: {produto_cadastrado[2]} | Preço: R$ {produto_cadastrado[3]:.1f}')
    
    return produto_cadastrado

def adicionar_um_produto(cliente, estoque_temporario):
    from UTIL.util_gestao_pedido import solicitar_quantidade, atualizar_estoque_temporario
    
    produto = obter_produto(cliente, estoque_temporario)
    if not produto:
        return None
            
    quantidade_escolhida, estoque_restante = solicitar_quantidade(produto)
    if quantidade_escolhida is None:
        return None
        
    atualizar_estoque_temporario(produto[0], quantidade_escolhida, estoque_temporario)

    estoque_restante_real = (
        produto[0],
        produto[1],
        quantidade_escolhida,
        produto[3],
        estoque_restante
    )
        
    return estoque_restante_real