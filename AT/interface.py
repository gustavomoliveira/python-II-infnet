from tabulate import tabulate
from validacao import *
from CRUD.crud_produto import *
from CRUD.crud_compras import *
from CRUD.crud_cliente import *

def menu():
    opcao = validar_opcao(
        '\n=========== Caixa Supermercado ===========\n\n'
        '[1] - Iniciar Atendimento\n'
        '[2] - Exibir Estoque\n'
        '[0] - Fechar Caixa\n'
        '\n===========================================\n'
        '\nEscolha uma opção para iniciar: '
    )
    return opcao

def iniciar_atendimento():
    id_cliente = validar_inteiro('\nInsira o ID do cliente para realizar a pesquisa: ')
    cliente = consultar_cliente(id_cliente)
    
    if not cliente:
        cliente = cadastrar_novo_cliente()
        if cliente is None:
            return 0, None

    print(f'\n===== Atendimento iniciado para o {cliente[1]} =====')

    produtos = consultar_todos_produtos()
    produtos_pedido = []
    
    while True:
        print(f'\nQual produto deseja adicionar ao pedido do {cliente[1]}?')
        produto = validar_disponibilidade_produto(produtos)

        if produto is not None:
            while True:
                quantidade = validar_inteiro(f'\nDigite a quantidade do {produto[1]} desejada: ')
                resto_estoque, quantidade_escolhida = validar_qtde_produto(quantidade, produto)

                if resto_estoque is not False:
                    break

            produto_atualizado = (produto[0], produto[1], quantidade_escolhida, produto[3], resto_estoque)
            produtos_pedido.append(produto_atualizado)
            
            if produto[0] > 0:
                for i, p in enumerate(produtos):
                    if p[0] == produto[0]:
                        produtos[i] = produto_atualizado
                        break
            else:
                produtos.append(produto_atualizado)

        opcao = validar_escolha('\nDeseja adicionar mais produtos ao pedido? ([1] - Sim / [2] - Finalizar Atendimento): ')
        if opcao == 2:
            print('\nInserção de produtos finalizada.')
            break

    print(f'\nA compra do {cliente[1]} foi concluída com sucesso! Retornando ao menu inicial.')

    incluir_compra(cliente)
    compra_atual = consultar_compra_atual()
    
    organizar_produtos_bd(produtos_pedido, compra_atual)

    soma_total = finalizar_atendimento(cliente, compra_atual)
    return soma_total, cliente
            
def finalizar_atendimento(cliente, compra):
    produtos = []
    tabela_resumida = []
    soma_total = 0
    itens = consultar_item(compra)
    
    for item in itens: 
        produto = consultar_produto(item[-1])
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