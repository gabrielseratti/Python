def unique_in_order(sequence):
    lista = []
    a = [0]

    for x in sequence:
        if x != a[-1]:
            lista.append(x)
            a.append(x)
        else:
            pass
    return lista

print(unique_in_order('AAAABBBCCDAABBB'))