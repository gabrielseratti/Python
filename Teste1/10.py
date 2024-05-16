def square_digits(num):
    if isinstance(num, int):
        lista = ''
        strin = f'{num}'
        for x in strin:
            a = int(x)
            a *= a
            lista += f'{a}'
        
        return lista
    else:
        return 
    
print(square_digits(811181))