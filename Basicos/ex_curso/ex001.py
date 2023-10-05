num =input('Digite um numero inteiro: ')
if num.isdigit():
    #função isdigit: verifica se o que foi difitado é um número!  
    num_int = int(num)
    if num_int % 2 == 0:
        print('É par!')
    else:
        print('É ímpar!')
else:
    print('Você não digitou um número inteiro!')
