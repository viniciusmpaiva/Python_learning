#Forma rapida para criar listas a partir de iteráveis
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

#Em list comprehension

lista_1 = [
    numero *2 
    for numero in range(10)
    ]

#Posso fazer operações dentro da list comprehension
print(lista_1)




