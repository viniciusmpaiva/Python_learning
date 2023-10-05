#Try e except:
"""
Funciona como um if, porém se houver algum erro no codigo
ele ja pula pro except
"""
numero_str = input('Numero a ser dobrado: ')

try:
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float *2}')
except:
    print('Isso não é um número!')