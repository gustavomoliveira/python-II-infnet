from arquivo import *
from utilitario import *

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('produtos.json')
    df_produtos = ler_arquivo(arquivo_entrada)
    df_produtos_ajustados = reajustar_preco(df_produtos, 5)
    gravar_arquivo(arquivo_entrada, df_produtos_ajustados)