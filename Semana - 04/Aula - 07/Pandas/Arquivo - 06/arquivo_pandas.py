import os, pandas as pd

NOME = 0
NOTA1 = 1
NOTA2 = 2
APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    df_turma = None
    try:
        df_turma = pd.read_csv(arq, encoding='UTF-8')
        #df_turma = pd.read_csv(arq, encoding='UTF-8'. header=None) --> caso não haja header no csv
        #df_turma.columns = ['Nome', 'Nota 1', 'Nota 2'] --> para especificar nomes de colunas
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return df_turma

def verificar_aprovacao(turma):
    aprovacao = []
    for aluno in turma:
        media = round(sum(aluno[1:]) / 2, 1)
        if media >= APROVACAO:
            aprovacao.append([aluno[NOME], media, 'Aprovado'])
        else:
            aprovacao.append([aluno[NOME], media, 'Prova Final'])
    return aprovacao

def gravar_arquivo(arq, aprovacao):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            aprovacao_csv = csv.writer(arquivo) # também possui delimiter
            aprovacao_csv.writerow(['Nome', 'Media', 'Status']) # gravando cabeçalho
            for aluno in aprovacao:
                aprovacao_csv.writerow(aluno)
            print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.csv')
df_turma = ler_arquivo(arquivo_entrada)
print(df_turma)


""" aprovacao = verificar_aprovacao(turma)
arquivo_saida = definir_arquivo('aprovacao.csv')
gravar_arquivo(arquivo_saida, aprovacao) """