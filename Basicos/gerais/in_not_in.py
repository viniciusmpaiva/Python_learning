nome = 'Vincius'
#Strings são iteráveis (podem ser acessada pelo índice)
#print(nome[2])
#in confere se tal coisa esta entre as letras da string
print('i' in nome)
print('a' in nome)
print('cius' in nome)
#not in faz o inverso,  verifica se não esta
print('cius' not in nome)
print('a' not in nome)

nome_1 = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')