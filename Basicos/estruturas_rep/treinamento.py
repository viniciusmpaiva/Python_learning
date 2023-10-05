frase = 'O python é uma linguagem de programação'\
        'Multiparadigma'\
        'Python foi criado por Guido van Rossum'

i = 0
mais_vezes = 0
letra_mais_vezes =''
while i < len(frase):
    letra_atual = frase [i]
    qtd_vezes = frase.count(letra_atual)
    i += 1
    if letra_atual == ' ':
        continue
    if qtd_vezes > mais_vezes:
        mais_vezes = qtd_vezes
        letra_mais_vezes = letra_atual
    i += 1


print(f'A letra que apareceu mais vezes é {letra_mais_vezes}'
      f' aparecendo {mais_vezes} vezes'
    )