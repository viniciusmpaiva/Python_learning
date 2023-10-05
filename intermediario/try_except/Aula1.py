
# try:
#     a=18
#     b = 0
#     print('Linha 1')
#     c = a/b #Aqui ocorre uma excessão
#     print('Linha 2')
#     #A linha 2 não é executada
#     #Erro silenciado - Má prática
# except:
#     print('Dividiu por 0')

# print('Continuar')

#O que se deve fazer:
#passar o nome do erro no except

try:
    a=18
    b = 0
    # print(b[0])
    print('Linha 1')
    c = a/b
except ZeroDivisionError as e:
    print(e)
except NameError:
    print('Nome b não definido')
except(TypeError,IndexError) as error:
    print('Type Error + Index Error')
    print('Msg:',error)
    print('Nome:',error.__class__.__name__)#Nome da classe da excessão
except Exception:
    #Trata qualquer erro
    print('Erro desconhecido')