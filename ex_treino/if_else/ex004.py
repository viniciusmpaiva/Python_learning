#Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
inteiro_1 = int(input('Digite o 1o inteiro: '))
inteiro_2 = int(input('Digite o 2o inteiro: '))
inteiro_3 = int(input('Digite o 3o inteiro: '))
if  inteiro_1>inteiro_2 and inteiro_2 > inteiro_3:
    print(f'O maior número é o {inteiro_1} e o menor é o {inteiro_3}')
elif inteiro_1>inteiro_2 and inteiro_2<inteiro_3 and inteiro_1>inteiro_3:
    print(f'O maior número é o {inteiro_1} e o menor é o {inteiro_2}')
elif inteiro_2>inteiro_1 and inteiro_1>inteiro_3:
    print(f'O maior número é o {inteiro_2} e o menor é o {inteiro_3}')
elif inteiro_2>inteiro_1 and inteiro_1<inteiro_3 and inteiro_2>inteiro_3:
    print(f'O maior número é o {inteiro_2} e o menor é o {inteiro_1}')
elif inteiro_3>inteiro_1 and inteiro_1>inteiro_2:
    print(f'O maior número é o {inteiro_3} e o menor é o {inteiro_2}')
elif inteiro_3>inteiro_1 and inteiro_1<inteiro_2 and inteiro_2 < inteiro_3:
    print(f'O maior número é o {inteiro_3} e o menor é o {inteiro_1}')

    