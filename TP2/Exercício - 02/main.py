import os, csv

ID = 0
NOME = 1
QTDE = 2
PRECO = 3

def definir_arquivo(nome_arquivo):
    diretorio = os.path.dirname(__file__)
    arq = os.path.join(diretorio, nome_arquivo)
    return arq

def ler_arquivo(arq):
    produtos = []
    try:
        with open(arq, 'r', encoding='UTF-8') as arquivo:
            produtos_csv = csv.reader(arquivo)
            next(produtos_csv)
            for produto in produtos_csv:
                produtos.append([int(produto[ID]), produto[NOME], int(produto[QTDE]), int(produto[PRECO])])
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return produtos

def reajustar_preco(produtos, percentual):
    for produto in produtos:
        produto[PRECO] *= 1 + (percentual / 100)
    return produtos

def gravar_arquivo(arq, produtos):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            produtos_csv = csv.writer(arquivo)
            produtos_csv.writerow(['id', 'nome', 'quantidade', 'preço'])
            for produto in produtos:
                produtos_csv.writerow(produto)
            print('Arquivo gravado com sucesso.')
    except:
        print(f'Erro na gravação do arquivo.')

if __name__ == '__main__':
    arquivo_entrada = definir_arquivo('produtos.csv')
    produtos = ler_arquivo(arquivo_entrada)
    produtos_ajustado = reajustar_preco(produtos, 5)
    gravar_arquivo(arquivo_entrada, produtos_ajustado)