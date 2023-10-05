lista = [1,2,56,76,89,999,80,89,54,67,4,5,32,12,13,14,56,76,78,91,13,1,5,44]

i=1
maior_valor = 0
temp = 0
while i <=(len(lista)-1):
    if lista[i-1]>lista[i]:
        temp = lista[i]
        lista[i] = lista[i-1]
        lista[i-1] = temp
    else:
        continue
    i+=1
    
j=0
while j<=(len(lista)-1):
        print(lista[j])