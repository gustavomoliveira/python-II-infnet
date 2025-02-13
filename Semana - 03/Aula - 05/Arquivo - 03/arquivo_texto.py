import os

nome_arquivo = 'nomes.txt'
diretorio_corrente = os.path.dirname(__file__)
ARQ = os.path.join(diretorio_corrente, nome_arquivo)

def ler_arquivo():
    nomes = []
    try:
        with open(ARQ, 'r', encoding='UTF-8') as arquivo:
            while linha := arquivo.readline():
                nomes.append(linha.strip('\n'))
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return nomes

def converter_nomes(nomes):
    nomes_convertidos = []
    for nome in nomes:
        nome_sobrenome = nome.split(' ')
        nomes_convertidos.append(nome_sobrenome[1].upper() + ', ' + nome_sobrenome[0])
    return nomes_convertidos

def gravar_arquivo(nomes):
    try:
        with open(ARQ, 'w', encoding='UTF-8') as arquivo:
            for nome in nomes:
                arquivo.write(nome + '\n')
    except:
        print('Erro na gravação do arquivo.')
        
nomes = ler_arquivo()
nomes = converter_nomes(nomes)
gravar_arquivo(nomes)