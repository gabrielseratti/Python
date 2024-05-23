def add_check_digit(number_checked):
    factor_checked = [7, 6, 5, 4, 3, 2]
    factor = factor_checked[::-1]
    number = number_checked[::-1]
    lista = []
    soma = 0

    i = 0
    while len(number) > len(lista):
        for x in factor:
            if len(number) == len(lista):
                break
            if i > len(factor)-1:
                i = 0
            lista.append(factor[i])
            i += 1

    for mult in range(len(number)):
        soma += int(number[mult]) * lista[mult]

    div = soma % 11

    if div == 0:
        return number[::-1] + '0';
    
    elif div == 1:
        return number[::-1] + 'X';

    else:
        return number[::-1] + f'{11 - div}'


print(add_check_digit('036532'))