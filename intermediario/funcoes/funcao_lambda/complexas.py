def executa(funcao,*args):
    return funcao(*args)

def soma(x,y):
    return x + y


#Os três são a mesma coisa
print(
    executa(
        lambda x,y: x+y,
        2,3
    ),
    executa(soma,2,3),
    soma(2,3)
)

#Ambas são a mesma coisa

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(
    lambda m: lambda n: n*m,
    2
)

print(duplica(2))


#pode usar args em lambda
print(
    executa(
        lambda *args:sum(args),
        1,2,3,4,5,6,6
    )
)

#Lambda é para coisas simples, não para coisas assim