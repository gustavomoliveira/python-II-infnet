from arquivo import *
from atendimento import *

produtos = ler_produtos()
cliente = 1
itens, total_compra = atender_cliente(produtos)
fechar_atendimento(cliente, itens, total_compra)