lista = [[1, 'Produto 1', 10], [2, 'Produto 2', 20], [3, 'Produto 3', 30]] # mutável, permite el repetido, existe ordenação
lista[0][2] = 15
#print(lista)

tupla = (1, 2, 3) # imutável, permite el repetido, existe ordenação
#tupla[0] = 15
#print(tupla)

dic = {1: ['Produto 1', 10], 2: ['Produto 2', 20], 3: ['Produto 3', 30]} # mutável, permite el repetido com excessão das chaves, existe ordenação
#print(dic)

# Conjunto
# não permite el repetido
# não existe ordenação
# declaração com chaves, assim como o dic
c1 = {1, 2, 3, 4}
c2 = {1, 5, 3, 7}

print(c1)
print(c2)
print()
print(c1 | c2) # união de conjuntos
print(c1.union(c2)) # outra forma de união utilizando método
print()
print(c1 & c2) # interseção de conjuntos
print(c1.intersection(c2)) # outra forma de interseção
print()
print(c1 - c2) # diferença(o que tem no 1 e não no 2)
print(c1.difference(c2)) # outra forma de diferença
print(c2 - c1)
print()

num = 3
print('Existe') if num in c1 else print('Não existe')

for el in c1:
    print(el)

