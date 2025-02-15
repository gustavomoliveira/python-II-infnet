import os

nome_arquivo = 'nomes.txt'
diretorio_corrente = os.path.dirname(__file__)
ARQ = os.path.join(diretorio_corrente, nome_arquivo)

def incluir_linha(nome):
    try:
        with open(ARQ, 'a', encoding='UTF-8') as arquivo:
            arquivo.write('\n' + nome)
    except:
        print('Erro na inclusão do arquivo.')

incluir_linha('Marcos Oliveira')