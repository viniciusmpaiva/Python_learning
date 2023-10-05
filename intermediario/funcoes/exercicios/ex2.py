def par_impar(num):
    if num %2 == 0:
        return True
    else:
        return False
num_digitado = int(input('Digite um número: '))
if par_impar(num_digitado) is True:
    print(f'O número {num_digitado} é par')
else:
    print(f'O número {num_digitado} é ímpar')