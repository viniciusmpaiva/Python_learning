#Keyword arguments (argumentos nomeados)
#retorna um dict com os argumentos nomeados(chaves) e valores
#Os não nomeados vão para args
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados: ',args)


    for chave,valor in kwargs.items():
        print(chave,valor)

mostro_argumentos_nomeados(1,2,nome = 'Joana', qualquer = 123)