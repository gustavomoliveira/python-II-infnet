import os, pandas as pd
from tabulate import tabulate
from conectar_bd import *
from validacoes import *
from crud_db import *
from util import *

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def criar_df(arq):
    df = None
    try:
        df = pd.read_csv(arq, header=None, encoding='UTF-8')
    except Exception as ex:
        print(f'\nERRO: O arquivo não pode ser lido: {ex}.')
        exit()
    return df

def inserir_dados_iniciais(df, query):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        df = df.iloc[:, 1:]
        dados = []

        for valores in df.values:
            dados.append(tuple(valores))
        cursor.executemany(query, dados)
        conn.commit()
    except Exception as ex:
        print(f'\nERRO: O arquivo não pode ser inserido: {ex}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

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

def abrir_caixa():
    if not consultar_dados_inseridos():
        arq_produtos = definir_arquivo('produtos.csv')
        arq_clientes = definir_arquivo('clientes.csv')
        df_produtos = criar_df(arq_produtos)
        df_clientes = criar_df(arq_clientes)

        query_produtos = """ INSERT INTO mercado_at.produto (nome, quantidade, preco)
            VALUES (%s, %s, %s) """
        inserir_dados_iniciais(df_produtos, query_produtos)

        query_clientes = """ INSERT INTO mercado_at.cliente (nome)
            VALUES (%s) """
        inserir_dados_iniciais(df_clientes, query_clientes)

    total_vendas = []
    while True:
        opcao = menu()
        match opcao:
            case 1:
               soma_total = iniciar_atendimento()
               total_vendas.append(soma_total)
            case 2:
                exibir_estoque(consultar_estoque_final())
            case 0:
                fechar_caixa(total_vendas)
                break
            case _:
                print('\nERRO: Opção inválida.')
            

def iniciar_atendimento():
    id_cliente = validar_inteiro('\nInsira o ID do cliente para realizar a pesquisa: ')
    cliente = consultar_cliente(id_cliente)

    if not cliente:
        opcao = validar_escolha('\nDeseja cadastrar o cliente no sistema? ([1] - Sim / [2] - Não): ')
        if opcao == 2:
            print('\nEncerrando Atendimento ao Cliente.')
            return
        else:
            nome_cliente = validar_nome('\nInsira o nome do cliente a ser cadastrado: ')
            print(f'\n{nome_cliente} cadastrado com sucesso no sistema.')
            cliente = incluir_cliente(nome_cliente)

    print(f'\n===== Atendimento iniciado para o {cliente[1]} =====')

    produtos = consultar_todos_produtos()
    while True:
        print(f'\nQual produto deseja adicionar ao pedido do {cliente[1]}?')
        produto = validar_disponibilidade_produto(produtos)

        if produto is not None:
            if produto[0] > len(produtos):
                produtos.append(produto)

            while True:
                quantidade = validar_inteiro(f'\nDigite a quantidade do {produto[1]} desejada: ')
                resto_estoque, quantidade_escolhida = validar_qtde_produto(quantidade, produto)

                if resto_estoque is not False:
                    break

            produto = (produto[0], produto[1], quantidade_escolhida, produto[3], resto_estoque)
            
            for i, tupla in enumerate(produtos):
                if tupla[0] == produto[0]:
                    produtos[i] = produto
                    break

        opcao = validar_escolha('\nDeseja adicionar mais produtos ao pedido? ([1] - Sim / [2] - Não): ')
        if opcao == 2:
            print('\nInserção de produtos finalizada.')
            break

    print(f'\nA compra do {cliente[1]} foi concluída com sucesso! Retornando ao menu inicial.')

    incluir_compra(cliente)

    for produto in produtos:
        if len(produto) == 5:
            if produto[0] < 6:
                atualizar_produto(produto)
                incluir_item(produto[2], consultar_compra_atual(), produto)
            else:
                incluir_produto(produtos[-1])
                incluir_item(produto[2], consultar_compra_atual(), consultar_produto_nome(produtos[-1]))

    soma_total =  finalizar_atendimento(cliente, consultar_compra_atual())
    return soma_total
            
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

    print(f'\nItens: {qtde_items[0]}')
    print(f'Total: R${int(soma_total)}\n')
    print('===========================================\n')

    return soma_total

def exibir_estoque(estoque):
    print(estoque)
    sem_estoque = [produto for produto in estoque if produto[1] == 0]
    
    if sem_estoque:
        print('\n===========================================\n')
        print('Produtos sem estoque:')
        for produto in sem_estoque:
            print(f'\n{produto[0]}')
    else:
        print('\nTodos os produtos possuem estoque.\n')
        print('\n===========================================')
    
def fechar_caixa(total_vendas):
    clientes_atendidos = []
    dados_caixa_fechado = []
    compras = consultar_compras()

    for id_cliente in compras:
        clientes_atendidos.append(consultar_cliente(id_cliente[2]))

    print('\n===========================================\n')
    print('Fechamento do Caixa')
    print(f'Data: {validar_data_hora()}\n')

    for cliente, total in zip(clientes_atendidos, total_vendas):
        dados_caixa_fechado.append([cliente[1], total])
        
    if len(dados_caixa_fechado) > 0:
        print(tabulate(dados_caixa_fechado, headers=['Cliente', 'Total']))
        print(f'\nTotal de Vendas: R${int(sum(total_vendas))}')
        print('\n===========================================\n')
        exibir_estoque(consultar_estoque_final())
    else:
        print('Não houveram vendas neste Caixa durante o dia de hoje.\n')


abrir_caixa()


