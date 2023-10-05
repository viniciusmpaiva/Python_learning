#Métodos:
# len - quantas chaves
#keys - Iterável com as chaves
#values - Iterável com os valores
#values - Iterável com chave e valores
#setdefault - adiciona valor se a chave não existe


pessoa = {
    'nome': 'Vinicius Paiva',
    'sobrenome':'Moraes',
}

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

pessoa.setdefault('idade', 0)
print(pessoa['idade'])


