import os

def definir_arquivo(nome_arquivo):
    diretorio = os.path.dirname(__file__)
    arq = os.path.join(diretorio, nome_arquivo)
    return arq

def ler_arquivo(arq):
    nomes = []
    try:
        with open(arq, 'r', encoding='UTF-8') as arquivo:
            while True:
                linha = arquivo.readline().strip('\n')
                if linha == '':
                    break
                nomes.append(linha)
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return nomes

def ordenar_nomes(nomes):
    return sorted(nomes)

def gravar_nomes(arq, nomes_ordenados):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            for nome in nomes_ordenados:
                arquivo.write(nome + '\n')
            print('Gravação realizada com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('nomes.txt')
    nomes = ler_arquivo(arquivo_entrada)
    nomes_ordenados = ordenar_nomes(nomes)
    gravar_nomes(arquivo_entrada, nomes_ordenados)
