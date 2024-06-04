def alphabet_position(text):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    retorno = []

    for letra in text:
        if letra.lower() in alfabeto:
            # print(f'{alfabeto.index(letra)} {letra}') 
            retorno.append(alfabeto.index(f'{letra.lower()}')+1)
        else:
            pass
    
    retorno_lista = ' '.join(map(str, retorno))

    return retorno_lista

print(alphabet_position("The sunset sets at twelve o' clock."))