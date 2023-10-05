import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width= 40)

produtos = [
    {'nome':'p1','preço':20, },
    {'nome':'p2','preço':10, },
    {'nome':'p3','preço':30, },
]

novos_produtos = [
    {**produto,'preço': produto['preço'] *1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos 
    if produto['preço']>10
]
#Print mais detalhado
p(novos_produtos)

#Filtro vem depois do for e não tem else
lista = [n for n in range(10) if n<5]
print(lista)