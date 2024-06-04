def rot13(message):
    alfa1 = "abcdefghijklm"
    alfa2 = "nopqrstuvwxyz"
    mensagem = ''

    for letter in message:
        if letter.isupper():
            if letter.lower() in alfa1:
                mensagem += alfa2[alfa1.index(letter.lower())].upper()
            if letter.lower() in alfa2:
                mensagem += alfa1[alfa2.index(letter.lower())].upper()
        if letter.islower():
            if letter in alfa1:
                mensagem += alfa2[alfa1.index(letter)]
            if letter in alfa2:
                mensagem += alfa1[alfa2.index(letter)]
        if letter.lower() not in alfa1 and letter not in alfa2:
            mensagem += letter
    return mensagem

print(rot13('This is actually the first kata IV ever made. Thanks for finishing it! :)'))