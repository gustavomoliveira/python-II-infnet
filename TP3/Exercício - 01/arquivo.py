import os, pandas as pd

def definir_arquivo(nome_arquivo):
    diretorio_atual = os.path.dirname(__file__)
    arq = os.path.join(diretorio_atual, nome_arquivo)
    return arq

def ler_arquivo(arq):
    try:
        df_produtos = pd.read_excel(arq)
        df_produtos['preco'] = df_produtos['preco'].astype(float)
    except Exception as ex:
        print(f'Erro na leitura do arquivo: {ex}.')
        exit()
    return df_produtos

def gravar_arquivo(arq, df_produtos, df_reajuste):
    try:
        with pd.ExcelWriter(arq) as writer:
            df_produtos.to_excel(writer, sheet_name='Antes', index=False)
            df_reajuste.to_excel(writer, sheet_name='Depois', index=False)
        print('Arquivo gravado com sucesso.')
    except Exception as ex:
        print(f'Erro na gravação do arquivo: {ex}.')