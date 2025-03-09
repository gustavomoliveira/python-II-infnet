def reajustar_precos(df_produtos):
    PERCENTUAL = 5
    df_produtos['preco'] = round(df_produtos['preco'] * (1 + (PERCENTUAL / 100)), 2)
    return df_produtos