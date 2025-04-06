import os, pandas as pd
from conectar_bd import *
from CRUD_BD.dados_bd import *

def definir_arquivo(nome_arquivo, pasta='CSV'):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, pasta, nome_arquivo)
    return arq

def criar_df(arq):
    df = None
    try:
        df = pd.read_csv(arq, header=None, encoding='UTF-8')
    except Exception as ex:
        print(f'\nERRO: O arquivo não pode ser lido: {ex}.')
        exit()
    return df

def carregar_dados_iniciais():
    arq_produtos = definir_arquivo('produtos.csv')
    arq_clientes = definir_arquivo('clientes.csv')

    df_produtos = criar_df(arq_produtos)
    df_clientes = criar_df(arq_clientes)

    query_produtos = """
        INSERT INTO mercado_at.produto (nome, quantidade, preco)
        VALUES (%s, %s, %s)
    """
    importar_dados_iniciais_bd(df_produtos, query_produtos)

    query_clientes = """
        INSERT INTO mercado_at.cliente (nome)
        VALUES (%s)
    """
    importar_dados_iniciais_bd(df_clientes, query_clientes)