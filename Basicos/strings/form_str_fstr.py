"""
> - Esquerda
< -  Direita
^ - Centro

"""
var = 'ABC'
print(f'{var}')
print(f'{var: >10}')#deixará 7 espaços para a esquerda
print(f'{var: <10}')#deixará 7 espaços para a direita
print(f'{var: ^10}')#deixará no meio de 10 espaços
#Qualquer coisa pode ser colocada após o ":", o que toma o lugar dos espaços 
#nos exemplos
print(f'{1000000.78387466776:+,.2f}')
#O + indica pro python mostrar o sinal de + se o número
#for positivo
print(f'O hexadecimal de 1500 é {1500:04x}')