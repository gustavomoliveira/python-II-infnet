import pandas as pd

def reajustar_precos(df_produtos):
    PERCENTUAL = 5
    df_reajuste = pd.DataFrame(columns=['id', 'nome', 'quantidade', 'preco_reajustado'])
    for _, produto in df_produtos.iterrows():
        preco_reajustado = round(produto['preco'] * (1 + (PERCENTUAL / 100)), 2)
        df_reajuste.loc[len(df_reajuste)] = [produto['id'], produto['nome'], produto['quantidade'], preco_reajustado]
    return df_reajuste