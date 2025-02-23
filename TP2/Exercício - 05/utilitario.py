def reajustar_preco(produtos, percentual):
    produtos['preço'] = round(produtos['preço'] * (1 + (percentual / 100)), 2)
    return produtos