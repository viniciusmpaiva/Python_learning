"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                                : R$   55,00 
    (-) INSS ( 10%)                       : R$  110,00
    FGTS (11%)                            : R$  121,00
    Total de descontos                : R$  165,00
    Salário Liquido                       : R$  935,00
"""
valor_hora = float(input('Valor da hora: '))
qtd_horas = int(input('Quantidade de horas trabalhadas: '))
sal = valor_hora*qtd_horas
if sal<=900:
    desc = 'Isento'
    ir = '0'
elif sal <=1500:
    desc = sal *0.05
    novo_sal = sal - desc
    ir='5%'
elif sal <=2500:
    desc = sal * 0.1
    novo_sal = sal - desc
    ir = '10%'
else:
    desc = sal*0.2
    novo_sal = sal - desc
    ir='20%'
inss = sal*0.1
fgts = sal*0.11
total_desc = desc + inss
sal_liq = sal -total_desc
print(f'Salário Bruto: ({qtd_horas} * {valor_hora})     : R${sal:.2f}')
print(f'(-) IR ({ir})                                   : R${desc:.2f}')
print(f'(-) INSS (10%)                                  : R${inss:.2f}')
print(f'FGTS (11%)                                      : R${fgts:.2f}')
print(f'Total de descontos                              : R${total_desc:.2f}')
print(f'Salário Liquido                                 : R${sal_liq:.2f} ')