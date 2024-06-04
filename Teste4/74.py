def solve(a,b):
    contagem = 0
    lista = ['8', '5', '3']
    for num in range(a, b):
        for x in str(num):
            if x not in lista:
                break
            if str(num).count('8') < str(num).count('5') or str(num).count('5') < str(num).count('3'):
                break
        else:
            contagem += 1
    return contagem

print(solve(34, 220789))