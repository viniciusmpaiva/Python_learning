# Exercício
# Crie uma função que encontra o primeiro duplicado considerando o segundo
# número como a duplicação. Retorne a duplicação considerada.
# Requisitos:
#     A ordem do número duplicado é considerada a partir da segunda
#     ocorrência do número, ou seja, o número duplicado em si.
#     Exemplo:
#         [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#         [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#         [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#     Se não encontrar duplicados na lista, retorne -1

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],#0 - -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],#1 - 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],#2 - 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],#3 - 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],#4 - 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],#5 - 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],#6 - 2 
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],#7 - 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],#8 - 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],#9 - 2 
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],#10 - 5
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],#11 - -1
]

def verificar_dup(lista,indice):
    set_copia = set()
    nao_duplicado = -1
    for i in range(len(lista[indice])):
        set_copia.add(lista[indice][i])
    if len(set_copia) != len(lista[indice]): 
        nao_duplicado = 0    
    return nao_duplicado

def encontrar_dup(lista,indice):
    menor_indice = len(lista[indice]) -1
    for i in range(len(lista[indice])):
        x=lista[indice][i]
        j=1
        while j<len(lista[indice]):
            if x == lista[indice][j] and j>i:
                if j< menor_indice:
                    menor_indice = j
            j+=1
    return lista[indice][menor_indice]                


for i in range(len(lista_de_listas_de_inteiros)):
    duplicado = verificar_dup(lista_de_listas_de_inteiros,i)
    if duplicado == -1:
        print(duplicado)
    else:
        primeiro_dup = encontrar_dup(lista_de_listas_de_inteiros,i)
        print(f'{i}) {primeiro_dup}')

#Outra resolução

def econtrar_duplicado(lista):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)

    return primeiro_duplicado
    
for lista in lista_de_listas_de_inteiros:
    print(econtrar_duplicado(lista))
