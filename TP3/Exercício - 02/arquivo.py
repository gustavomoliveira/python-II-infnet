import os, pandas as pd, glob

def definir_arquivo(nome_arquivo):
    diretorio_atual = os.path.dirname(__file__)
    arq = os.path.join(diretorio_atual, nome_arquivo)
    return arq

def ler_arquivo(arqs):
    df_produtos = pd.DataFrame()
    try:
        for arq in glob.glob(arqs):
            df = pd.read_excel(arq)
            df_produtos = pd.concat([df, df_produtos], axis=0, ignore_index=True)
        df_produtos['preco'] = df_produtos['preco'].astype(float)
    except Exception as ex:
        print(f'Erro na leitura do arquivo: {ex}.')
        exit()
    return df_produtos

def gravar_arquivo(arq, df_reajuste):
    try:
        with pd.ExcelWriter(arq) as writer:
            df_reajuste.to_excel(writer, sheet_name='Produtos', index=False)
        print('Arquivo gravado com sucesso.')
    except Exception as ex:
        print(f'Erro na gravação do arqquivo: {ex}.')