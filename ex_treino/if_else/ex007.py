"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = input('Digite o turno em que você estuda: ')
if turno == 'manhã' or turno == 'Manhã':
    print('Bom Dia!')
elif turno == 'tarde' or turno == 'Tarde':
    print('Boa Tarde!')
elif turno == 'noite' or turno == 'Noite':
    print('Boa Noite!')
else:
    print('Valor Inválido!')