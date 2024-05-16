def digital_root(n):
    a = str(n)
    lista = []
    for x in a:
        lista.append(int(x))
    s = sum(lista)
    if n < 10:
        return n
    else:
        return digital_root(s)
        
print(digital_root(132189))
    

# def digital_root(n):
    # a = map(int, str(n))
    # if n < 10:
    #     return n
    # else:
    #     return digital_root(sum(map(int,str(n))))

