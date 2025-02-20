import os, json

def definir_arquivo(nome_arquivo):
    diretorio = os.path.dirname(__file__)
    arq = os.path.join(diretorio, nome_arquivo)
    return arq

def ler_arquivo(arq):
    produtos = None
    try:
        with open(arq, 'r', encoding='UTF-8') as arquivo:
            produtos = json.load(arquivo)
    except:
        print('Erro na leitura do arquivo')
        exit()
    return produtos

def reajustar_preco(produtos, percentual):
    for produto in produtos:
        produto['preço'] *= round(1 + (percentual / 100), 2)
    return produtos

arquivo_entrada = definir_arquivo('produtos.json')
produtos = ler_arquivo(arquivo_entrada)
produtos_ajustado = reajustar_preco(produtos, 5)
print(produtos_ajustado)
