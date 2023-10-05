import os
lista_compras=[]
while True:
    erro = 0
    op = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ').lower()
    inserir = op.startswith('i')
    apagar = op.startswith('a')
    listar = op.startswith('l')

    if inserir is True:
        item_inserido = input('Valor: ')
        lista_compras.append(item_inserido)
        erro=1
    if apagar is True:
        apagar_indice = int(input('Digite o índice do item a ser apagado: '))
        lista_compras.pop(apagar_indice)
        erro =1
    if listar is True:
        for indice ,item in enumerate(lista_compras):
            os.system('cls')
            print(indice, item)
        erro =1
    if erro ==0:
        print('Digite uma opção válida')

        
