#Funções anonimas que contem apenas uma linha 
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['sobrenome']

#"Ensina" o python a ordenar
l1 = sorted(lista,key=lambda item:item['nome'])
l2 = sorted(lista,key=lambda item:item['sobrenome'])

def imprimir(lista):
    for item in lista:
        print(item)
    print()
    
imprimir(l1)
imprimir(l2)