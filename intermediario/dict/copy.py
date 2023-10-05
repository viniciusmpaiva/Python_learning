import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}
#Ambas as variáveis apontam para o mesmo dicionario
#não copia!
#d2 = d1

# - shallow copy(Cópia raza):
#Copia os valores imutáveis, já os mutáveis ele faz com que 
#os dois dicionários apontem para a mesma lista na memória
d2 = d1.copy()
# print(d2)
d1['l1'][0] = 9
print(d2,d1)

#-Deep copy:

d1 = copy.deepcopy(d1)