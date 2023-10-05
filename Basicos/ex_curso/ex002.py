hour = int(input('Digite a hora atual: '))
if hour <=11 :
    print('Bom Dia!')
elif hour <=17 :
    print('Boa Tarde!')
elif hour <=23:
    print('Boa Noite!')
else: 
    print('Hora inválida')