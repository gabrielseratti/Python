def divisors(integer):
    lista = []
    for x in range(2, integer):
        if integer % x == 0:
            lista.append(x)
    if len(lista) == 0:
        return f'{integer} is prime'
    return lista

print(divisors(15))