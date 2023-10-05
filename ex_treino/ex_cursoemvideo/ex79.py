
l = []
nao_existe = -1
ja_existe = -2
erro = -3
n_vezes = 0

def adicionar():
    num_adc = input('Digite o valor: ')
    num_adc_check = num_adc.isnumeric()
    if num_adc_check is False:
        print('Erro! Digite um número')
        return erro
    for num in l:
        if num_adc == num:
            print('Valor duplicado! Não vou adicionar...')
            return 
    l.append(num_adc)
    return l

def bubble_sort(lista):
    temp = 0
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j+1]:
                temp = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temp
    return lista

while True:
    if n_vezes == 0:
        lista = adicionar()
        n_vezes =1 
        continue
    op = input('Quer continuar? [S/N] ').lower()
    if op == 's':
        lista = adicionar() 
    elif op == 'n':
        lista_fixed = bubble_sort(lista)
        print(lista_fixed)
        break
    else:
        print('Opção inválida!\n')
        continue

    