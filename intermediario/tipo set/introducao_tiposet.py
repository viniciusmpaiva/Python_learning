# conjunto
# sets em python são mutáveis porém aceitam apenas tipos imutaveis
#pode colocar um iterável 
s1 = set() #Vazio tem que ser desse jeito
s2 = {'Vinicius',1,2,3}
print(s1)
print(s2)

#São eficientes para remover valores dupilcados de iteráveis
s3 = {1,2,3,4,3,3,3,1,5}
print(s3)

#EX
l1 = [1,2,3,4,5,5,4,3,3,3,6,1,1,1,2]
#Retirar os valores repetidos da lista
s4 = set(l1)
l2 = list(s4)
print(l2)

#Não garantem ordem
#Não tem indice

 