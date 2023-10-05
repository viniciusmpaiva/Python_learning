import os

palavra_secreta = 'santos'
letras_acertadas=''
string = ''
tentativas = 0

while True:

    letra_digitada = input('Digite uma letra: ')

    tamanho_letra_digitada = len(letra_digitada)

    if tamanho_letra_digitada != 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas+=letra_digitada

    palavra_formada =''

    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada+=letra
        else:
            palavra_formada+='*'

    print(palavra_formada)

    tentativas+=1
    if palavra_formada == palavra_secreta:
        os.system('cls')       
        print('PARABÉNS, VOCÊ ACERTOU!!!!')
        print(f'Numero de tentativas: {tentativas}')

        letras_acertadas=''
        tentativas =-0


    


    