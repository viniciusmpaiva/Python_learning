produto = {
    'nome': 'Caneta Azul',
    'preço': 2.5,
    'categoria':'escritorio',
}

# for chave,valor in produto.items():
#     print(chave,valor)

dc = {
    chave:valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dc)