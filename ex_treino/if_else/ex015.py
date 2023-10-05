#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
if mes > 12 or dia > 31 or mes<1 or dia <1 or ano <1:
    print('A data não é válida!')
    print()

elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia >31) or (mes ==2 and dia >28) or (mes ==4 and dia >30) or (mes==6 and dia > 30) or (mes==9 and dia>30) or (mes == 11 and dia > 30):
        print('A data não é válida!')
else:
      print(f'A data {dia}/{mes}/{ano} é válida!')
