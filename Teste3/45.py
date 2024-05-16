def move_zeros(lst):
    lista = []
    lista_de_zeros = []
    for x in lst:
        if x == 0:
            lista_de_zeros.append(x);
        else:
            lista.append(x);
    return lista + lista_de_zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))