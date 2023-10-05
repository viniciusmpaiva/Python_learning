#Generator Functions
#Funções que sabem pausar

def generator(n=0):
    yield 1 #Pausa
    #Trocar o return pelo yield
    # return 'ACABOU'
    #O return levanta uma excessão de stop iteration
    # Se acabou já o yield, é ativada    
    print('Continuando...')
    yield 2
    print("Mais uma vez")
    yield 3
    print('Vou terminar')
    return 'Acabouu'

gen = generator(n=0)
#Imprime o valor de yield
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)


def generator_1(n=0,max=10):
    while True:
        yield n
        n+=1
        if n>max:
            return


gen_1 = generator_1(max=10000)
for n in gen_1:
    print(n)
