def to_float_array(arr): 
    lista = []
    for x in arr:
        try:
            lista.append(int(x))
        except:
            lista.append(float(x))
    return lista

print(to_float_array(["1.1", "2", "3"]))