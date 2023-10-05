string = 'Vinicius'

metodo = 'upper'
print(string)


#hasattr - checa se determinado objeto possui determinado metodo
if hasattr(string,'upper'):
    print('Existe upper')
    print(string.upper())

#getattr - vai fazer a mesma coisa dinãmicamente

if hasattr(string,'upper'):
    print('Existe upper')
    print(getattr(string,metodo)())