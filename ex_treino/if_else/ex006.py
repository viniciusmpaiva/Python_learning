#Faça um Programa que leia três números e mostre-os em ordem decrescente
num1 = input('Digite o 1o número: ')
num2 = input('Digite o 2o número: ')
num3 = input('Digite o 3o número: ')
if num1>num2 and num2>num3:
    print(f'{num1},{num2},{num3}')
elif num1>num2 and num3>num2 and num1> num3:
    print(f'{num1}, {num3}, {num2}')
elif num2>num1 and num1>num3:
    print(f'{num2}, {num1}, {num3}')
elif num2>num1 and num3>num1 and num3<num2:
    print(f'{num2}, {num3}, {num1}')
elif num3> num1 and num1> num2:
    print(f'{num3}, {num1}, {num2}')
elif num3> num1 and num2>num1 and num3>num2:
    print(f'{num3}, {num2}, {num1}')