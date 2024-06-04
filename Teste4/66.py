def persistence(n):
    var = 0
    fac = 0
    i = -1
    while len(str(n)) != 1:
        fac += 1
        for x in str(n):
            if i == len(str(n))-1:
                n = var
                i = -1
                break
            if i < 0:
                i += 1
                var = int(x)
            else:
                i += 1
                var *= int(x)
    return fac/2


print(persistence(999))