def spot_diff(s1, s2):
    i = -1
    lista = []
    for letters in zip(s1, s2):
        i += 1
        if letters[0] != letters[1]:
            lista.append(i)
    return lista

print(spot_diff("abcdefg", "abcqetg"))