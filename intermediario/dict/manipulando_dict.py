pessoa = {}

# pessoa['nome'] = 'Vinicius Paiva'

#Chaves dinâmicas

chave = 'nome'
pessoa[chave] = 'Vinicius Paiva'
print(pessoa)
pessoa[chave] = 'Maria'

del pessoa['nome']
print(pessoa)


#Não existe, ocorre excessão, como contornar?
if pessoa.get('sobrenome') is None:
    print('Não Existe!')
else:
    print('Existe')
