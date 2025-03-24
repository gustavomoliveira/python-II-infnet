import os, pandas as pd
from tabulate import tabulate
from conectar_bd import *
from validacoes import *
from crud_db import *

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def criar_df(arq):
    df = None
    try:
        df = pd.read_csv(arq, header=None, encoding='UTF-8')
    except Exception as ex:
        print(f'Erro na leitura do arquivo: {ex}.')
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
        print('Valores inseridos com sucesso.')
    except Exception as ex:
        print(f'Erro na inserção dos dados: {ex}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def menu():
    opcao = input(
        '===== Caixa Supermercado =====\n\n'
        '[1] - Iniciar Atendimento\n'
        '[2] - Finalizar Atendimento\n'
        '[3] - Fechar Caixa\n'
        '\n=============================\n'
        'Escolha uma opção para iniciar: '
    )
    return opcao

def abrir_caixa():
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

    opcao = menu()

def iniciar_atendimento():
    cliente = consultar_cliente()

    if not cliente: # TODO --> alterar ordem condicional
        opcao = validar_escolha('\nDeseja cadastrar o cliente no sistema? ([1] - Sim / [2] - Não): ')
        if opcao == 1:
            cliente = incluir_cliente()
        else:
            print('\nEncerrando Atendimento ao Cliente.')
            #TODO --> finalizar_atendimento()
            #finalizar_atendimento()

    print(f'\n===== Atendimento iniciado para o cliente: {cliente[1]} =====')
    incluir_compra(cliente)
    compra = consultar_compra()
    print(f'\nQual produto deseja adicionar ao pedido do {cliente[1]}?')
    id = validar_inteiro('\nInsira o ID do produto para consultar sua disponibilidade em estoque: ')
    produto = consultar_produto(id)
    consultar_estoque(produto)
    qtde_produto = selecionar_produto(produto)
    
    while True:
        opcao = validar_escolha('Deseja adicionar mais produtos ao pedido? ([1] - Sim / [2] - Não): ')
        if opcao == 2:
            print('Inserção de produtos finalizada.')
            break
        else:
            id = validar_inteiro('\nInsira o ID do produto para consultar sua disponibilidade em estoque: ')
            produto = consultar_produto(id)
            qtde_produto = selecionar_produto(produto)
            incluir_item(qtde_produto, compra, produto)
    
    #finalizar_atendimento()
            
def finalizar_atendimento(cliente, compra):
    item = consultar_item(compra)
    produto = consultar_produto(item[3])
    qtde_items = consultar_qtde_items()
    total = produto[3] * item[1]
    #TODO --> criar loop em itens
    colunas_tabela = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']
    tabela_resumida = [item[0], produto[1], item[1], total]

    print('\n===========================================')
    print(f'\nCliente {cliente[1]}\n')
    print(f'Data: {validar_data_hora()}\n')

    print(tabulate(tabela_resumida, headers=colunas_tabela))

    print(f'\nItens: {qtde_items}')
    print(f'Total: {soma_total}\n')
    print('===========================================\n')