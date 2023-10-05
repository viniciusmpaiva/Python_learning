x = 1

def escopo():
    # global x#Permite a manipulação da variavel fora do escopo
    #O x global é a mesma variavel de fora do escopo
    print(x)
    def outra_funcao(): 
        x = 11
        y=2
        print(y,x) 
    print(x)
    outra_funcao()

# print(x)
escopo()
# print(x)

