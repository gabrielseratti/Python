def next_higher(n):
    gg = 0
    gg2 = str(bin(n)[0] + bin(n)[2:]).count('1')
    x = n+1
    print(bin(n)[0] + bin(n)[2:])
    while gg != gg2:
            gg = str(bin(x)[0] + bin(x)[2:]).count('1')
            if gg == gg2:
                return f'{x} => {int(bin(x)[0] + bin(x)[2:])}'
            x += 1

print(next_higher(912076743    ))