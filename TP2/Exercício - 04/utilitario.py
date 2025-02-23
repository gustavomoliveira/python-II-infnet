def reajustar_preco(produtos, percentual):
    produtos['preço'] *= 1 + (percentual / 100)
    return produtos