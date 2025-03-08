import pandas as pd
from conectar_db import *

APROVACAO = 6

def ler_banco(banco):
    sql = 'SELECT * FROM aluno'
    try:
        engine = conectar(banco)
        df_turma = pd.read_sql(sql, engine)
    except Exception as ex:
        print(f'Erro na abertura do arquivo: {ex}.')
        exit()
    finally: # certo ou errado, finally é executado
        desconectar(engine)
    return df_turma

def verificar_aprovacao(df_turma):
    df_aprovacao = pd.DataFrame(columns=['nome', 'media', 'status'])
    for _, aluno in df_turma.iterrows():
        media = round((aluno['nota1'] + aluno['nota2']) / 2, 1)
        if media >= APROVACAO:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Aprovado']
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Prova Final']
    return df_aprovacao

def gravar_aprovacao(banco, df_aprovacao):
    try:
        engine = conectar(banco)
        df_aprovacao.to_sql('aprovacao', engine, if_exists='replace', index=False)
        print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')
    finally:
        desconectar(engine)

banco = definir_banco('turma.db')
verificar_banco(banco)
df_turma = ler_banco(banco)
print(df_turma)
print(df_turma.dtypes)
df_aprovacao = verificar_aprovacao(df_turma)
print(df_aprovacao)
gravar_aprovacao(banco, df_aprovacao)
