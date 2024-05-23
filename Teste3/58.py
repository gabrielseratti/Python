def duplicate_encode(word):
    letras = []
    letras_duplicadas = []
    retorno = ''
    for x in word.lower():
        if x not in letras:
            letras.append(x)
        else:
            letras_duplicadas.append(x)

    for x in word.lower():
        if x in letras_duplicadas:
            retorno += ')'
        else:
            retorno += '('

    return retorno
    #your code here

print(duplicate_encode('Success'))