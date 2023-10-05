frase = 'Olha só, que coisa interessante '
lista_frases_raw= frase.split(',')



lista_frases_fixed = []

#Não é recomendado fazer deste jeito
for i,frase in enumerate(lista_frases_raw):
    lista_frases_fixed.append(lista_frases_raw[i].strip())
#strip() - corta espaço do começo e do fim da string
#rstrip - corta o espaço da direita
#lstrip - corta o espaço da esquerda
print(lista_frases_fixed)
print(lista_frases_raw)
#join - Une strings

frases_unidas = ', '.join(lista_frases_fixed)
print(frases_unidas)
