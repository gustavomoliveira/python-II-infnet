import time
import sys

#TAM = 100_000_001 # é possível usar esse tipo de notação em py para determinar casas decimais
TAM = 1_000_000

ID = TAM - 1

def criar_lista():
    lista = []
    for i in range(1, TAM):
        produto = [i, "Produto " + str(i), i]
        lista.append(produto)
    return lista

def pesquisar_lista(lista, id):
    for produto in lista:
        if (produto[0] == id):
            return produto
    return None

def criar_dic():
    dic = {}
    for i in range(1, TAM):
        dic[i] = ["Produto " + str(i), i]
    return dic

def pesquisar_dic(dic, id):
    return dic[id]

print("Criação da lista")
inicio = time.process_time()
lista = criar_lista()
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
inicio = time.process_time()
print("Pesquisando lista")
produto = pesquisar_lista(lista, ID)
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)
lista.clear()

print()
print("Criação do dicionário")
inicio = time.process_time()
dic = criar_dic()
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print("Pesquisando dicionário")
inicio = time.process_time()
produto = pesquisar_dic(dic, ID)
fim = time.process_time()
print('Tempo em seg.:', fim - inicio)
print(produto)
