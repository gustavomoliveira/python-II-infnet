import os, pandas as pd

def definir_arquivo(nome_arquivo):
    diretorio = os.path.dirname(__file__)
    arq = os.path.join(diretorio, nome_arquivo)
    return arq

def ler_arquivo(arq):
    df_produtos = None
    try:
        df_produtos = pd.read_csv(arq, encoding='UTF-8', delimiter=';', dtype={'preço': float})
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return df_produtos

def gravar_arquivo(arq, produtos):
    try:
        produtos.to_csv(arq, index=False, sep=';')
        print('Arquivo atualizado com sucesso.')
    except:
        print('Erro ao atualizar o arquivo.')