string = 'Python'
string_size = len(string)
numbers = range(0, string_size +1 )
for number in numbers:
    print(number)

for i in range(10):
    if i ==2:
        print('i é 2, pulando...')
        continue

    '''if i ==8:
        print('i é 8, else não é executado')
        break'''

    for j  in range(1,3):
        print(i, j)
else:
    print('For completo com sucesso')