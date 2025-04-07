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
            return

    print(f'\n===== Atendimento iniciado para o {cliente[1]} =====')

    produtos_pedido = adicionar_produtos_pedido(cliente)

    if not produtos_pedido:
        print('\nNenhum produto foi adicionado ao pedido.')
        return

    print(f'\nA compra do {cliente[1]} foi concluída com sucesso! Retornando ao menu inicial.')

    incluir_compra(cliente)
    compra_atual = consultar_compra_atual()

    organizar_produtos(produtos_pedido, compra_atual)
    finalizar_atendimento(cliente, compra_atual)
            
def finalizar_atendimento(cliente, compra):
    tabela_resumida = []
    soma_total = 0
    
    itens_detalhados = consultar_resumo_compra_bd(compra[0])
    
    for i, item in enumerate(itens_detalhados, start=1):
        nome_produto = item[0]
        quantidade = item[1]
        preco = item[2]
        subtotal = item[3]
        soma_total += subtotal
        tabela_resumida.append([i, nome_produto, quantidade, preco, subtotal])

    colunas_tabela = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']

    print('\n===========================================')
    print(f'\n{cliente[1]}')
    print(f'Data: {validar_data_hora()}\n')

    print(tabulate(tabela_resumida, headers=colunas_tabela))

    print(f'\nItens: {len(itens_detalhados)}')
    print(f'Total: R${int(soma_total)}\n')
    print('===========================================\n')

def exibir_estoque():
    sem_estoque = consultar_produtos_sem_estoque_bd()
    
    if sem_estoque:
        print('\n===========================================\n')
        print('Produtos sem estoque:')
        for produto in sem_estoque:
            print(f'\n{produto[0]}')
    else:
        print('\nTodos os produtos possuem estoque.\n')
    
    print('\n===========================================')
    
def fechar_caixa():
    print('\n===========================================\n')
    print('Fechamento do Caixa')
    print(f'Data: {validar_data_hora()}\n')
    
    dados_caixa = consultar_resumo_diario_bd()
    
    if dados_caixa:
        print(tabulate(dados_caixa, headers=['Cliente', 'Total']))
        total_vendas = sum(item[1] for item in dados_caixa)
        print(f'\nTotal de Vendas: R${int(total_vendas)}')
        print('\n===========================================\n')
        exibir_estoque()
    else:
        print('Não houveram vendas neste Caixa durante o dia de hoje.\n')