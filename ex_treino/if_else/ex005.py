#Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela
var_1 = input('Digite o 1o inteiro: ')
var_2 = input('Digite o 2o inteiro: ')
print(f'{var_1=} {var_2=}')
temp = var_1
var_1 = var_2
var_2 = temp
print(f'{var_1=} {var_2=}')