def operacoes(multiplicador):
    def multiplicar(num):
        return multiplicador*num
    return multiplicar

multiplicar_2 = operacoes(2)
multiplicar_3 = operacoes(3)
multiplicar_4 = operacoes(4)

num_recebido = int(input('Digite um número a ser multiplicado: '))

print(f'{num_recebido} * 2 = {multiplicar_2(num_recebido)}')
print(f'{num_recebido} * 3 = {multiplicar_3(num_recebido)}')
print(f'{num_recebido} * 4 = {multiplicar_4(num_recebido)}')

