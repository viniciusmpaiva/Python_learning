name = input('Digite o seu nome: ')
name_cont = len(name)
if name_cont>1:
    if name_cont<=4:
        print('Seu nome é curto')
    elif name_cont<=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite um nome!')