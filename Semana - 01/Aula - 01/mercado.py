from arquivo import *
from atendimento import *
from caixa import *

FECHAR_CAIXA = 2

produtos = ler_produtos()
clientes = []
cliente = 0
opcao = menu_caixa()
while opcao != FECHAR_CAIXA:
    itens, total_compra = atender_cliente(produtos)
    if itens:
        cliente += 1
        fechar_atendimento(cliente, itens, total_compra)
        clientes.append([cliente, total_compra])
    opcao = menu_caixa()
if clientes:
    fechar_caixa(clientes)
    verificar_estoque(produtos)
    #gravar_produtos()

fechar_caixa(clientes)
