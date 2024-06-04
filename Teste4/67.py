def relatively_prime (n, l):
    factors_list = []
    factors = []
    result = []
    for x in range(2, n+1):
        if n % x == 0:
            factors_list.append(x)
    for num in l:
        for x in range(1, num+1):
            if num % x == 0:
                factors.append(x)
        if not bool(set(factors) & set(factors_list)):
            result.append(num)
        factors = []

    return result

print(relatively_prime(3, [21, 4, 25, 26, 4, 4, 24, 23, 72, 82]))