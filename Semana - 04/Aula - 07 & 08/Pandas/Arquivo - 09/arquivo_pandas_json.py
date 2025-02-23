import os, pandas as pd

APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    df_turma = None
    try:
        df_turma = pd.read_json(arq, encoding='UTF-8')
        #df_turma[['notas'][0], ['notas'][1]] = df_turma[['notas'][0], ['notas'][1]].astype(float)
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return df_turma

def verificar_aprovacao(df_turma):
    df_aprovacao = pd.DataFrame(columns=['nome', 'media', 'status']) #criando novo dataframe
    for _, aluno in df_turma.iterrows():
        media = round((aluno['notas'][0] + aluno['notas'][1]) / 2, 1)
        if media >= APROVACAO:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Aprovado']
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Prova Final']
    return df_aprovacao

def gravar_arquivo(arq, df_aprovacao):
    try:
        df_aprovacao.to_json(arq, orient='records', indent=4, force_ascii=False)
        print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.json')
df_turma = ler_arquivo(arquivo_entrada)
print(df_turma)
print(df_turma.dtypes)
df_aprovacao = verificar_aprovacao(df_turma)
print(df_aprovacao)
arquivo_saida = definir_arquivo('aprovacao.json')
gravar_arquivo(arquivo_saida, df_aprovacao)