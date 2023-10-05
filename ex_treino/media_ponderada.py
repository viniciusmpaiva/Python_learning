import os
notas=[]
i=0
funcao = lambda x,y:(x+y)/2

def conceito(media):
    if media<5:
        return 'D'
    elif media<7:
        return 'C'
    elif media<9:
        return 'B'
    else:
        return 'A'

while i<10:
    nota1 = input(f'Digite a nota 1 do {i} aluno: ')
    if not nota1.isdecimal():
        print('Digite um número!')
        continue
    
    nota1_num = float(nota1)
    
    if nota1_num >10 or nota1_num<0:
        print('Inválidos!')
        continue

    nota2 = input(f'Digite a nota 2 do {i} aluno: ')
    if not nota2.isdecimal():
        print('Digite um número!')
        continue
    
    nota2_num = float(nota2)
    
    if nota2_num >10 or nota2_num <0:
        print('Inválidos!')
        continue
    

    media = funcao(nota1_num,nota2_num)
    nota_final = conceito(media)
    notas.append(nota_final) 
    i+=1
    os.system('cls')

os.system('cls')
for j in range(10):
    print('=-'*30)
    print(f'\nAluno {j} - Nota: {notas[j]}\n')
    print('=-'*30)


    