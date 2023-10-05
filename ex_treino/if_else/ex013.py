"""
 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
 O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
    sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)
"""
import math
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
if a ==0:
    print('A equação não é de segundo grau')
    print()
else:
    delta = (b**2) - 4*a*c
    if delta<0:
        print('A equação não possui raízes reais!')
        print()
    elif delta == 0:
        raiz = -b/(2*a)
        print(f'A equação possui apenas uma raíz real, sendo essa: {raiz}') 
    else:
        raiz_1 = (-b + math.sqrt(delta))/(2*a)
        raiz_2 = (-b - math.sqrt(delta))/(2*a)
        print(f'A equação possui duas raízes reais, sendo estas: {raiz_1} e {raiz_2}')
