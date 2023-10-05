#generator - Função que pausa em determinado local
import sys

lista = [n for n in range(10000000)]
print(sys.getsizeof(lista))
#Vê a ocupação de memória da lista
#List Comprehension
#Muitos dados na memória

generetor_1 = (n for n in range(10000000))
print(sys.getsizeof(generetor_1))

#O generator não esta na memória como a lista, esta esperando

print(next(generetor_1))

for n in generetor_1:
    print(n)

# Desvantagens - Não tem tamanho nem indice
#impossivel acessar índice