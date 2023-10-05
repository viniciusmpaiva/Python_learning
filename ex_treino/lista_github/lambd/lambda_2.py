# Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar
num = int(input('Digite um número: '))
par_impar = lambda x: x%2

result_str = 'par' if par_impar(num) == 0 else 'ímpar'

print(f'O número é {result_str}')