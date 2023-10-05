dados_pessoa = {
    'idade': 16,
    'altura':1.88
}

def mostro_argumentos_nomeados(*args,**kwargs):
    
    for chave,valor in kwargs.items():
        print(chave,valor)

config = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
}

mostro_argumentos_nomeados(**config)