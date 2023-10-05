#Faça um Programa que leia três números inteiros e mostre o maior deles
inteiro_1 = input('Digite o 1o número inteiro: ')
inteiro_2 = input('Digite o 2o número inteiro: ')
inteiro_3 = input('Digite o 3o número inteiro: ')
if (inteiro_1>inteiro_2 and inteiro_1>inteiro_3):
    print(f'O maior numero é o {inteiro_1}')
elif inteiro_2>inteiro_1 and inteiro_2>inteiro_3:
    print(f'O maior numero é o {inteiro_2}')
elif inteiro_3>inteiro_2 and inteiro_3>inteiro_1:
    print(f'O maior número é o {inteiro_3}')