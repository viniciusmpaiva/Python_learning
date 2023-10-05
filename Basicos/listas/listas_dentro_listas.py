#listas de listas e seus indices
salas = [
    ['Maria','Helena', ],#0
    ['Elaine', ],#1
    ['Luiz','João', 'Eduarda',],#2
]
print(salas[0][1])
print(salas[2][2])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)