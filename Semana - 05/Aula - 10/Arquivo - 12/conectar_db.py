import os
from sqlalchemy import create_engine

def definir_banco(nome_banco):
    diretorio_corrente = os.path.dirname(__file__)
    banco = os.path.join(diretorio_corrente, nome_banco)
    return banco

def conectar(banco):
    try:
        engine = create_engine('sqlite:///' + banco)
        print('Banco conectado.')
    except Exception as ex:
        print(f'Erro ao conectar o banco: {ex}')
        exit()
    return engine