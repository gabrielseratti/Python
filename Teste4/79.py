def difference_of_squares(n):
    lista_square = []
    lista_sum = []
    for x in range(1,n+1):
        lista_square.append(x)
        lista_sum.append(x*x)
    
    return sum(lista_square)*sum(lista_square)-sum(lista_sum)

print(difference_of_squares(10))