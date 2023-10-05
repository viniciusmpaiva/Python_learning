
lista = []

def insert_list(qtd):
    i=0
    while i<=qtd-1:
        valor = int(input(f'Digite um valor para a posição {i}: '))
        lista.append(valor)
        i+=1
    print('\n','='*30)
    return lista

def maior_menor():

    qtd = int(input('Digite a quantidade de valores a serem alocados à lista: '))
    lista = insert_list(qtd)
    maior = 0
    maior_indice = 0
    menor_indice = 0
    menor = 0
    for indice,item in enumerate(lista):
        if indice == 0:
            maior = menor = item
        else:
            if item > maior:
                maior = item
                maior_indice = indice
            if item < menor:
                menor = item
                menor_indice = indice

    print(f'Você digitou os valores {lista}\nO maior valor digitado foi {maior} na posição {maior_indice}\n\
O menor valor digitado foi {menor} na posição {menor_indice}')

maior_menor()
