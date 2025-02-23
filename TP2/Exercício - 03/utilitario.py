def reajustar_preco(produtos, percentual):
    for produto in produtos:
        produto['preço'] = round(produto['preço'] * (1 + (percentual / 100)), 2)
    return produtos