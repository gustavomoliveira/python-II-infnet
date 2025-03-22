import os, pandas as pd
from mysql.connector import Error
from conectar_bd import *
from validacoes import *

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

def consultar_cliente():
    id = validar_inteiro('\nInsira o ID do cliente: ')
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'SELECT nome FROM mercado_at.cliente WHERE id_cliente = %s'
        cursor.execute(query, (id,))
        cliente = cursor.fetchone()

        if cliente:
            print(f'\nCliente encontrado: {cliente[0]}.')
        else:
            print('\nCliente não encontrado.')
        return cliente
    
    except Error as e:
        print(f'\nERRO: Não foi possível realizar a busca: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def cadastrar_cliente():
    nome = input('\nInsira o nome do cliente a ser cadastrado: ')
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        query = 'INSERT INTO mercado_at.cliente (nome) VALUES (%s)'
        cursor.execute(query, (nome,))
        conn.commit()
        print('\nNovo cliente inserido com sucesso!')
    except Exception as ex:
        print(f'\nErro na inserção dos dados: {ex}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()   

def iniciar_atendimento():
    cliente = consultar_cliente()

    if not cliente:
        opcao = validar_escolha('\nDeseja cadastrar o cliente no sistema? [1] - Sim / [2] - Não')
        if opcao == 1:
            cadastrar_cliente()
        else:
            finalizar_atendimento()



#TODO --> contruir finalizar_atendimento()


#abrir_caixa()
