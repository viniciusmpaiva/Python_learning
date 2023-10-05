#finally é um bloco que sempre será executado, mesmo que ocorra
#um erro

#else é executado caso o código seja executado sem erros
try:
    print(111)
    print('abrir arquivo')
    8/0

except ZeroDivisionError:
    print('Dividiu por zero')

else:
    print('Não deu erro')

finally:
    print(222)
    print('fechar arquivo')
