contador = 0

while contador <=100:
    contador+=1

    if contador == 6:
        continue

    """Serve para 'pular' um laço"""

    if contador >=10 and contador <= 27:
        print('Não vou motsrar o',contador)
        continue

    print(contador)

    if contador == 40:
        break