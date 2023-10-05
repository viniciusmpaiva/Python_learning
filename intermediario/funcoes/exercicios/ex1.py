def multiplica(*args):
    total = 1
    for num in args:
        total*=num
    return total
numeros = 1,2,3,5,7
conta = multiplica(*numeros)
print(conta)
