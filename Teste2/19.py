def spin_words(sentence):
    a = sentence.split(' ')
    y = ''
    lista = []
    print(a)
    for x in a:
        if len(x) > 4:
            x = ''.join(list(x)[::-1])
            lista.append(x) 
        else:
            lista.append(x)         
    return ' '.join(lista)

print(spin_words("Hey fellow warriors"))