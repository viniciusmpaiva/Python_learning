"""
 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input('Digite um número inteiro menor que 1000:' ))
unidade = num % 10
dezena = ((num - unidade)/10)%10
centena = (((num - unidade)/10)-dezena)/10
if centena == 0:
    if dezena == 0:
        if unidade==0:
            print('O número não possui dezena, centena nem unidade')
        elif unidade == 1:
            print(f'{num} = 1 unidade')
        else:
            print(f'{num} = {unidade} unidades')
    elif dezena ==1:
        if unidade ==1:
            print(f'{num} = 1 dezena e 1 unidade')
        else:
            print(f'{num} = 1 dezena e {unidade} unidades')
    else:
        if unidade==1:
            print(f'{num} = {dezena} dezenas e 1 unidade')
        else:
            print(f'{num} = {dezena} dezenas e {unidade} unidades')            
elif centena ==1:
    if dezena == 1:
        if unidade==1:
            print(f'{num} = 1 centena, 1 dezena e 1 unidade')
        else:
            print(f'{num} = 1 centena, 1 dezena e {unidade} unidades')
    else:
        if unidade == 1:
            print(f'{num} = 1 centena, {dezena} dezenas e 1 unidade')
        else:
            print(f'{num} = 1 centena, {dezena} dezenas e {unidade} unidades')
else:
    if dezena == 1:
        if unidade ==1:
            print(f'{num} = {centena} centenas, 1 dezena e 1 unidade')
        else:
            print(f'{num} = {centena} centenas, 1 dezena e {unidade} unidades')
    else:
        if unidade ==1:
            print(f'{num} = {centena} centenas, {dezena} dezenas e 1 unidade')
        else:
            print(f'{num} = {centena} centenas, {dezena} dezenas e {unidade} unidades')    
