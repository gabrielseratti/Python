def neutralise(s1, s2):
    s = ''
    for x, y in zip(s1, s2):
        if x != y:
            x, y = 0, 0

        s += str(x)

    return str(s)


print(neutralise("-++-", "-+-+"))