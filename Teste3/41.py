def count_sheep(n):
    s = ''
    for x in range(n+1):
        s += (f'{x} sheep...')
    return str(s)


print(count_sheep(55))