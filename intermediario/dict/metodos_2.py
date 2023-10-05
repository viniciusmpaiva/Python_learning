p1 = {
    'nome':'Luiz',
    'sobrenome': 'Miranda',
}

#get - Obtem uma chave
print(p1.get('nome'))

#pop - Apaga um ítem com a chave especificada

nome = p1.pop('nome')

#popitem - Apaga a ultima chave do dict

ultima_chave = p1.popitem()

#update - Atualiza o dicionário

p1.update({
    #atualizar valores, criar novas chaves
    'idade': 30,
})

p1.update(nome = 'novo valor', altura = 1.88)

tupla=('novo nome','novo valor'),
p1.update(tupla)
