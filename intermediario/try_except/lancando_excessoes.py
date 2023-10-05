#Erros podem ser manualmente lançados

# print(123)
# raise ValueError('Deu Erro')
# print(456)

# def divide(n,d):

#     try:
#         return n/d
#     except:
#         print('____')
#         raise
# #Fazer isso para fazer algo com o erro antes de dar a mensagem

def nao_pode_zero(d):
    if d ==0:
        raise ZeroDivisionError('Você esta dividindo por 0')


def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n,(float,int)):
        raise TypeError(
            f'{n} deve ser int ou float '
            f'"{tipo_n.__name__}" enviado'
        )




def divide_2 (n,d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)

    nao_pode_zero(d)
    return n/d



print(divide_2('8',0))