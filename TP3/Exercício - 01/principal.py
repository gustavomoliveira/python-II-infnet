from arquivo import *
from utilitario import *

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('produtos.xlsx')
    df_produtos = ler_arquivo(arquivo_entrada)
    df_reajuste = reajustar_precos(df_produtos)
    arquivo_saida = definir_arquivo('produtos2.xlsx')
    gravar_arquivo(arquivo_saida, df_produtos, df_reajuste)
