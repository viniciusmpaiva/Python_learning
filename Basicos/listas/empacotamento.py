nomes = ['Maria','Helena','Luiz']
nome1, nome2, nome3 = nomes
print(nome2)
##OUU

nomes_2 = ['Maria','Helena','Luiz']
nome4, nome5, nome6 = nomes_2
print(nome5)

#Caso queira pegar somente um valor
_,nome7,*_ = ['Maria', 'Helena', 'Luiz']
#Convenção pra variável que não bvai ser utilizada:(_)
print(nome7)