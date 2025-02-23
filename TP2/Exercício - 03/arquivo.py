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

def gravar_arquivo(arq, produtos):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            arquivo.write(json.dumps(produtos, indent=4, ensure_ascii=False))
            print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')