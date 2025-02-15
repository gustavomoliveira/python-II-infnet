# diretório absoluto
#ARQ = '/Users/gustavo/Desktop/Infnet/Python II/Semana - 03/Aula - 05/nomes.txt'

import os

# diretório relativo
nome_arquivo = 'nomes.txt'
diretorio_corrente = os.path.dirname(__file__) # pega o diretório de onde o programa está rodando
ARQ = os.path.join(diretorio_corrente, nome_arquivo)

def ler_arquivo_1():
    try:
        with open(ARQ, 'r', encoding='UTF-8') as arquivo: # with garante o fechamento automático do ARQ ao final
            linha = arquivo.readline()
            while linha != '':
                linha = linha.strip('\n') # remove o caractere oculto de pular linha
                print(linha)
                linha = arquivo.readline()
    except:
        print('Erro na abertura do arquivo.')
        exit()

def ler_arquivo_2():
    try:
        with open(ARQ, 'r', encoding='UTF-8') as arquivo:
            while linha := arquivo.readline():
                linha = linha.strip('\n')
                print(linha)
    except:
        print('Erro na abertura do arquivo.')
        exit()

def ler_arquivo_3():
    try:
        with open(ARQ, 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo.readlines():
                print(linha, end='')
    except:
        print('Erro na abertura do arquivo.')
        exit()

def ler_arquivo_4():
    try:
        with open(ARQ, 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                print(linha, end='')
    except:
        print('Erro na abertura do arquivo.')
        exit()


#ler_arquivo_1()
#ler_arquivo_2()
#ler_arquivo_3()
ler_arquivo_4()