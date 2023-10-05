# *args(empacotamento e desempacotamento)
def soma(*args):
    total=0
    for numero in args:
        total+=numero
    return total
        
soma_1_2_3=soma(1,2,3)
print(soma_1_2_3)
numeros = 4,5,6,7,8
#desempacotando
soma_4_5_6_7_8 = soma(*numeros)
print(soma_4_5_6_7_8)

#função sum() realiza a soma de um iterável

print(sum((4,5,6,7,8)))