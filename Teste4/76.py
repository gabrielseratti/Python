def sort_array(source_array):
    contador = 0
    for num1 in source_array:
        for num2 in source_array:
            contador += 1
            if num2 % 2 != 0 and num2 < num1:
                sub = num2
                source_array[source_array.index(num1)] = sub
                source_array[contador-1] = num1

    return source_array
                    


print(sort_array([5, 8, 6, 3, 4]))