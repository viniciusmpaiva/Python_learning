lista = [10, 20, 30, 40]

lista.append(50)# Adiciona elementos ao final da lista
lista.append(60)
lista.pop() #Apaga o ultimo elemento da lista
lista.pop(3) #Apaga o elemento do indice informado
lista.append(70)
del lista[-1]

lista.clear()#Limpa a lista

lista.insert(0, 5) #o 1 argumento é o indice e o segundo é o valor

print(lista)