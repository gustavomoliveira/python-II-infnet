import os, json

APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    turma = None
    try:
        with open(arq, 'r', encoding='UTF-8') as arquivo:
            turma = json.load(arquivo)
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return turma

def verificar_aprovacao(turma):
    aprovacao = []
    for aluno in turma:
        media = round(sum(aluno['notas']) / 2, 1)
        if media >= APROVACAO:
            aprovacao.append([aluno['nome'], media, 'Aprovado'])
        else:
            aprovacao.append([aluno['nome'], media, 'Prova Final'])
    return aprovacao

def gravar_arquivo(arq, aprovacao):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            arquivo.write(json.dumps(aprovacao, indent=4, ensure_ascii=False))
            print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.json')
turma = ler_arquivo(arquivo_entrada)
aprovacao = verificar_aprovacao(turma)
print(aprovacao)
arquivo_saida = definir_arquivo('aprovacao.json')
gravar_arquivo(arquivo_saida, aprovacao)