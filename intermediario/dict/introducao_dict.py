#Estruturas de dado do tipo chave e valor
#chave pode ser considerada como o "indice"
#pode ser de tipos imutáveis
#É como se fosse uma struct

pessoa = {
    'nome': 'Vinicius Paiva',
    'sobrenome':'Moraes',
    'idade': 18,
    'altura': 1.88,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': ' outra tal tal', 'número': 321}
    ],
}
#Também pode ser utilizado assim
#pessoa = dict(nome = 'Vinicius Paiva')
print(pessoa['nome'])
print(pessoa['endereços'])
for k in pessoa:
    print(k,pessoa[k])
