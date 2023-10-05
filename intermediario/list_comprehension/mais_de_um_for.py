# lista= []
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))
# print(lista)

lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
#Há também

lista_1 = [
    [(x,letra)for letra in 'Vinicius']
    for x in range(3)

]


print(lista)
print(lista_1)