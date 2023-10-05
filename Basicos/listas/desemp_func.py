string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria','Helena', ],#0
    ['Elaine', ],#1
    ['Luiz','João', 'Eduarda',],#2
]

'''print(*lista)
#pega cada um dos itens e passa separadamente
print(*string)
print(*tupla)'''

print(*salas, sep ='\n')