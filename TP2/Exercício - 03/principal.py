from arquivo import *
from utilitario import *

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('produtos.json')
    produtos = ler_arquivo(arquivo_entrada)
    produtos_ajustado = reajustar_preco(produtos, 5)
    gravar_arquivo(arquivo_entrada, produtos_ajustado)