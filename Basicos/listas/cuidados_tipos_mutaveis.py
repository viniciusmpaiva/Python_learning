lista_a = ['Luiz', 'Maria']
lista_b = lista_a
'''Nesse caso, não é copiado a lista a para a b, mas
    na verdade são criadas duas variaveis apontando
    para a mesma lista
    Quando algo é alterado em uma das variaveis, é al-
    terado na outra também
'''
lista_a[0] = 'Qualquer coisa'
print(lista_b)

#Para copiar uma lista para outra variavel:
lista_c = ['Vinicius','Cleber']
lista_d = lista_c.copy()

print(lista_d)