import pandas as pd
from conectar_db import *

def ler_banco(banco):
    sql = 'SELECT * FROM produto'
    try:
        engine = conectar(banco)
        df_produtos = pd.read_sql(sql, engine)
    except Exception as ex:
        print(f'Erro na abertura do arquivo: {ex}.')
        exit()
    finally:
        desconectar(engine)
    return df_produtos

def reajustar_precos(df_produtos):
    PERCENTUAL = 5
    df_produtos['preco'] = round(df_produtos['preco'] * (1 + (PERCENTUAL / 100)), 2)
    return df_produtos

def gravar_tabela(banco, df_reajuste):
    try:
        engine = conectar(banco)
        df_reajuste.to_sql('produto', engine, if_exists='replace', index=False)
        print('Arquivo gravado com sucesso.')
    except Exception as ex:
        print(f'Erro na gravação da tabela: {ex}.')
    finally:
        desconectar(engine)

if __name__ == '__main__':
    banco = definir_banco('mercado.db')
    df_produtos = ler_banco(banco)
    df_reajuste = reajustar_precos(df_produtos)
    gravar_tabela(banco, df_reajuste)