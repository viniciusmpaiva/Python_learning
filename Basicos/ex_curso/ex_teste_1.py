name = input('Digite o seu nome: ')
age = input('DIgite a sua idade: ')
if not name or not age:
    print('Desculpe, você deixou campos vazios')
else:
    t_name = name[::-1]
    print(f'Seu nome é: {name}')
    print(f'Seu nome invertido é: {t_name}')
    if ' ' in name:
        print('O seu nome contém espaços')
    else:
        print('O seu nome não contém espaço')
    print(f'O seu nome contém {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A ultima letra do seu nome é {name[len(name) - 1]}')

