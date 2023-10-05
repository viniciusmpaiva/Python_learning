# a, b = 1, 2
# a, b = b, a

pessoa= {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
# pessoa_2= {
#     'nome': 'Aline',
#     'sobrenome': 'Souza'
# }

# a,b = pessoa.values()
# print(a,b)

# (a1,a2), (b1,b2) = pessoa_2.items()
# print(a1,a2,b1,b2)

# for chave,valor in pessoa.items():
#     print(chave,valor)

dados_pessoa= {
    'idade':18,
    'altura': 1.88,
}
#Extrair os dados de um dict para outro
#posso continuar adicionando coisas
pessoa_completa = {**pessoa, 'chave':1}
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)
