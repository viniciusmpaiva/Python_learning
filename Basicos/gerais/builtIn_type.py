"""
    Tipos Imutáveis:
    -str, int, float, bool
"""
string = 'vinicius'
another_var = f'{string[:3]}ABC{string[4:]}'
print(string)
print(another_var)
"""
Metodos de String na doc do python
"""
"""EX: capitalize() = Primeira letra maiúscula"""
print(string.capitalize())
print(string.zfill(100))