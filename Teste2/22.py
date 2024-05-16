def square_sum(numbers):
    lista = []
    for x in numbers:
        x *= x
        lista.append(x)
        
        
    return sum(lista)

print(square_sum([1,2,2]))