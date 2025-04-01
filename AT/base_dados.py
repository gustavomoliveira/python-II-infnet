import os, pandas as pd
from conectar_bd import *

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

def importar_dados_iniciais(df, query):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        df = df.iloc[:, 1:]
        dados = [tuple(valores) for valores in df.values]
        cursor.executemany(query, dados)
        conn.commit()
        print(f"\nDados importados com sucesso! ({len(dados)} registros)")
        return True
    except Exception as ex:
        print(f'\nERRO: Os dados não puderam ser inseridos: {ex}.')
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()