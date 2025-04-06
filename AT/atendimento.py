from tabulate import tabulate
from UTIL.util_gestao_cliente import processar_cliente_inexistente
from UTIL.util_gestao_pedido import adicionar_produtos_pedido, organizar_produtos
from UTIL.util import validar_data_hora
from CRUD.crud_produto import *
from CRUD.crud_compra import *
from CRUD.crud_cliente import *
from CRUD.crud_item import *

def iniciar_atendimento():
    cliente = consultar_cliente()
    
    if not cliente:
        cliente = processar_cliente_inexistente()
        if cliente is None:
            return 0, None

    print(f'\n===== Atendimento iniciado para o {cliente[1]} =====')

    produtos_pedido = adicionar_produtos_pedido(cliente)

    if not produtos_pedido:
        print('\nNenhum produto foi adicionado ao pedido.')
        return 0, cliente

    print(f'\nA compra do {cliente[1]} foi concluída com sucesso! Retornando ao menu inicial.')

    incluir_compra(cliente)
    compra_atual = consultar_compra_atual()

    organizar_produtos(produtos_pedido, compra_atual)
    soma_total = finalizar_atendimento(cliente, compra_atual)

    return soma_total, cliente
            
def finalizar_atendimento(cliente, compra):
    produtos = []
    tabela_resumida = []
    soma_total = 0
    itens = consultar_item(compra)
    
    for item in itens:
        id_produto = item[-1]
        produto = consultar_produto(id_produto)
        produtos.append(produto)
    
    qtde_items = consultar_qtde_items(compra)

    for i, (produto, item) in enumerate(zip(produtos, itens), start=1):
        total = produto[3] * item[1]
        soma_total += total
        tabela_resumida.append([i, produto[1], item[1], produto[3], total])

    colunas_tabela = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']

    print('\n===========================================')
    print(f'\n{cliente[1]}')
    print(f'Data: {validar_data_hora()}\n')

    print(tabulate(tabela_resumida, headers=colunas_tabela))

    print(f'\nItens: {qtde_items}')
    print(f'Total: R${int(soma_total)}\n')
    print('===========================================\n')

    return soma_total

def exibir_estoque(estoque):
    sem_estoque = [produto for produto in estoque if produto[1] == 0]
    
    if sem_estoque:
        print('\n===========================================\n')
        print('Produtos sem estoque:')
        for produto in sem_estoque:
            print(f'\n{produto[0]}')
    else:
        print('\nTodos os produtos possuem estoque.\n')
    
    print('\n===========================================')
    
def fechar_caixa(total_vendas, clientes_atendidos):
    dados_caixa_fechado = []
    clientes_validos = []

    print('\n===========================================\n')
    print('Fechamento do Caixa')
    print(f'Data: {validar_data_hora()}\n')

    for cliente, total in zip(clientes_atendidos, total_vendas):
        if cliente is not None:
            clientes_validos.append((cliente, total))

    for cliente, total in clientes_validos:
        dados_caixa_fechado.append([cliente[1], total])
        
    if dados_caixa_fechado:
        print(tabulate(dados_caixa_fechado, headers=['Cliente', 'Total']))
        print(f'\nTotal de Vendas: R${int(sum(total_vendas))}')
        print('\n===========================================\n')
        exibir_estoque(consultar_estoque_final())
    else:
        print('Não houveram vendas neste Caixa durante o dia de hoje.\n')