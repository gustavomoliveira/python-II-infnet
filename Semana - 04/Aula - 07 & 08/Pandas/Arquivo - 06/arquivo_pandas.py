import os, pandas as pd

APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    df_turma = None
    try:
        df_turma = pd.read_csv(arq, encoding='UTF-8')
        #df_turma = pd.read_csv(arq, sep=';', encoding='UTF-8'. header=None) --> caso não haja header no csv e usando sep caso não seja ','
        #df_turma.columns = ['Nome', 'Nota 1', 'Nota 2'] --> para especificar nomes de colunas
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return df_turma

def verificar_aprovacao(df_turma):
    df_aprovacao = pd.DataFrame(columns=['nome', 'media', 'status']) #criando novo dataframe
    for _, aluno in df_turma.iterrows():
        media = round((aluno['nota1'] + aluno['nota2']) / 2, 1)
        if media >= APROVACAO:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Aprovado']
        else:
            df_aprovacao.loc[len(df_aprovacao)] = [aluno['nome'], media, 'Prova Final']
    return df_aprovacao

def gravar_arquivo(arq, df_aprovacao):
    try:
        df_aprovacao.to_csv(arq, index=False)
        print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.csv')
df_turma = ler_arquivo(arquivo_entrada)
df_aprovacao = verificar_aprovacao(df_turma)
arquivo_saida = definir_arquivo('aprovacao.csv')
gravar_arquivo(arquivo_saida, df_aprovacao)