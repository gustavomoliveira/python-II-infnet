import os, pandas as pd

APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    try:
        df_turma = pd.read_excel(arq)
        df_turma[['nota1', 'nota2']] = df_turma[['nota1', 'nota2']].astype(float)
    except Exception as ex:
        print(f'Erro na abertura do arquivo. {ex}')
        exit()
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

def gravar_arquivo(arq, df_turma, df_aprovacao):
    try:
        with pd.ExcelWriter(arq) as writer:
            df_turma.to_excel(writer, sheet_name='notas', index=False)
            df_aprovacao.to_excel(writer, sheet_name='aprovacao', index=False)
        print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.xlsx')
df_turma = ler_arquivo(arquivo_entrada)
print(df_turma)
print(df_turma.dtypes)
df_aprovacao = verificar_aprovacao(df_turma)
print(df_aprovacao)
arquivo_saida = definir_arquivo('turma2.xlsx')
gravar_arquivo(arquivo_saida, df_turma, df_aprovacao)