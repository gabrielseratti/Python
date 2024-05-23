import string

def high(str):
    alfabeto = []
    soma_palavra = []
    soma_letra = 0  
    
    a = str.split(' ')
    
    for letra in zip(string.ascii_lowercase, range(1, 27)):
        alfabeto.append(letra)

    for palavras in str:
        if palavras == ' ':
            soma_palavra.append(soma_letra)
            soma_letra = 0
        for letras in palavras:
                if letras in dict(alfabeto):
                    soma_letra += dict(alfabeto)[letras]
        # print(soma_palavra)
    soma_palavra.append(soma_letra)

    gg = []
    cont = -1
    for item in soma_palavra:
        cont += 1
        if item in gg:
            return a[cont]
        else:
             gg.append(item)
    return sum(soma_palavra)

              

    return soma_palavra

print(high('ab ab aa aaa'))