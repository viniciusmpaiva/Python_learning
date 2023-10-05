# Desenvolva uma calculadora rudimentar onde o usuário deve informar: qual operação ele deseja realizar,
#  quais os valores para a realização do cálculo (apenas dois valores) e o resultado da operação

soma = lambda x,y: x+y
subtracao = lambda x,y: x-y
divisao = lambda x,y: x/y
multiplicacao = lambda x,y: x*y
modulo = lambda x,y: x%y
validos = '+-*%/'

while True:
    operacao = input('Informe a operação desejada (+;-;*;/;%): ')
    prim_num = int(input('Informe o primeiro numero: '))
    seg_num = int(input('Informe o segundo numero '))

    if operacao not in validos:
        print('Informe a operação a ser realizada')
        continue

    if operacao == '+':
        print(soma(prim_num,seg_num))
    elif operacao == '-':
        print(subtracao(prim_num,seg_num))
    elif operacao == '*':
        print(multiplicacao(prim_num,seg_num))
    elif operacao == '%':
        try:
            print(modulo(prim_num,seg_num))
        except ZeroDivisionError:
            print('Inválido! Não pode dividir por 0')
            continue
    elif operacao == '/':
        try:
            print(divisao(prim_num,seg_num))
        except ZeroDivisionError:
            print('Inválido! Não pode dividir por 0')
            continue