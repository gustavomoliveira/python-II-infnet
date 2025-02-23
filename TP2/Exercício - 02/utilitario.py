from constantes import *

def reajustar_preco(produtos, percentual):
    for produto in produtos:
        produto[PRECO] *= 1 + (percentual / 100)
    return produtos