"""
Valores padrão para parâmetros:
Os parâmetros podem ter valores padrão. Caso o valor não seja enviado
para o parâmetro, o valor padrão será usado
"""

def soma(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}')
    else:
        print(f'{x=} {y=}')
soma(1,2,0)
