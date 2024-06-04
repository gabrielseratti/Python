def trigrams(phrase):
    lista = ''
    trigr = ''
    i = 0
    for x in phrase:
        a = 0
        for x in phrase[i: (i+3)]:
            if i > len(phrase)-3:
                lista = lista[0:-1]
                return lista
            if x == ' ':
                x = '_'
            if a < 3:
                trigr += x
                a += 1
        lista += trigr
        lista += ' '
        trigr = ''
        i += 1

print(trigrams("the quick red"))