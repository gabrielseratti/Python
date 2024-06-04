
def is_pangram(st):
    alfa = []
    for i in range(65, 91):
        alfa.append((chr(i)).lower())

    a = list(map(lambda letra: letra in alfa, filter(str.isalpha, st.lower())))

    try:
        b = list(map(lambda letra: alfa.remove(letra), filter(str.isalpha, st.lower())))
    finally:
        pass

    if a and alfa == []: return True
    else: return False
    return alfa
print(is_pangram("abcdefghijklm opqrstuvwxyz"))