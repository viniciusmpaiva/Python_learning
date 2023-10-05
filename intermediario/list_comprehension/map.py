produtos = [
    {'nome':'p1','preço':20, },
    {'nome':'p2','preço':10, },
    {'nome':'p3','preço':30, },
]

novos_produtos = [
    {**produto,'preço': produto['preço'] *1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos,sep='\n')