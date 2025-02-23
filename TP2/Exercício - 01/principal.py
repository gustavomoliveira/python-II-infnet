from arquivo import *
from utilitario import *

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('nomes.txt')
    nomes = ler_arquivo(arquivo_entrada)
    nomes_ordenados = ordenar_nomes(nomes)
    gravar_nomes(arquivo_entrada, nomes_ordenados)