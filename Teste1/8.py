def create_phone_number(n):
    parentes = ''
    num1 = ''
    num2 = ''
    for x in n:
        if len(parentes) == 0 or len(parentes) <= 2:
            parentes += str(x)
        elif len(num1) == 0 or len(num1) <= 2:
            num1 += str(x)
        elif len(num2) >= 6 or len(num2) <= 9:
            num2 += str(x)

    return f'({parentes}) {num1}-{num2}'
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))