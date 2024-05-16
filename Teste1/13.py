def repeat_str(repeat, string):
    lista = ''
    for i in range(repeat):
        lista += string
    return lista

print(repeat_str(11, 'String'))