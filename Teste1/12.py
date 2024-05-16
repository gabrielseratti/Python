def find_it(seq):
    count = 0
    lista = []
    for x in seq:
        if x not in lista:
            lista.append(x)
            count+=1
        else:
            lista.remove(x)  
    a = str(lista[0])
    return a

print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
