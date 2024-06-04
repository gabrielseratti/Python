def locker_run(lockers):
    lista = []
    open = [] 
    i = 0
    while lockers >= i:
        i += 1
        for x in range(0, lockers, i):
            if i == 1:
                lista.append(1)
            if lista[x] == 0:
                lista.insert(x, 1)
                lista.pop(x+1)
            else:
                lista.insert(x, 0)
                lista.pop(x+1)
    i = -1
    for x in lista:
        i += 1
        if x == 1:
            open.append(i)
    if open != []:
        if open[0] == 0:
            open.pop(0)
    return open

print(locker_run(6))