while True:
    num_1 = input('Informe o 1 numero: ')
    num_2 = input('Informe o 2 numero: ')
    op = input('Informe a operação a ser realizada(+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Número(s) inválido(s), tente novamente!')
        continue

    op_validos = '+-*/'

    if op not in op_validos:
        print('Operador inválido!, tente novamente')
        continue

    if len(op) >1:
        print('Operador inválido!, tente novamente')
        continue

    res = 0

    if op =='+':
        res = num_2_float + num_1_float
        print(f'{num_1_float} + {num_2_float} = {res}')
    elif op == '-':
        res = num_1_float - num_2_float
        print(f'{num_1_float} - {num_2_float} = {res}')
    elif op =='/':
        res = num_1_float / num_2_float
        print(f'{num_1_float} / {num_2_float} = {res}')
    else:
        res = num_1_float * num_2_float
        print(f'{num_1_float} * {num_2_float} = {res}')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print('Você saiu da calculadora!')
        break