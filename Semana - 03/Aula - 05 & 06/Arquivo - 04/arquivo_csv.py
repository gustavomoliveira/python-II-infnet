import os, csv

NOME = 0
NOTA1 = 1
NOTA2 = 2
APROVACAO = 6

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def ler_arquivo(arq):
    turma = []
    try:
        with open(arq, encoding='UTF-8') as arquivo:
            turma_csv = csv.reader(arquivo) # parâmetro opcional delimiter para ';'
            next(turma_csv) # pula o header (não conseguiria calcular strings do cabeçalho, por exemplo)
            for aluno in turma_csv:
                turma.append([aluno[NOME], float(aluno[NOTA1]), float(aluno[NOTA2])])
    except:
        print('Erro na abertura do arquivo.')
        exit()
    return turma

def verificar_aprovacao(turma):
    aprovacao = []
    for aluno in turma:
        media = round(sum(aluno[1:]) / 2, 1)
        if media >= APROVACAO:
            aprovacao.append([aluno[NOME], media, 'Aprovado'])
        else:
            aprovacao.append([aluno[NOME], media, 'Prova Final'])
    return aprovacao

def gravar_arquivo(arq, aprovacao):
    try:
        with open(arq, 'w', encoding='UTF-8') as arquivo:
            aprovacao_csv = csv.writer(arquivo) # também possui delimiter
            aprovacao_csv.writerow(['Nome', 'Media', 'Status']) # gravando cabeçalho
            for aluno in aprovacao:
                aprovacao_csv.writerow(aluno)
            print('Arquivo gravado com sucesso.')
    except:
        print('Erro na gravação do arquivo.')

arquivo_entrada = definir_arquivo('turma.csv')
turma = ler_arquivo(arquivo_entrada)
aprovacao = verificar_aprovacao(turma)
arquivo_saida = definir_arquivo('aprovacao.csv')
gravar_arquivo(arquivo_saida, aprovacao)