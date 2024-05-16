def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = ''
    for x in string_:
        if x.lower() not in vowels:
            text += x;
    return text


print(disemvowel("No offense but, Your writing is among the worst I've ever read"))