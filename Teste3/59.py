def find_even_index(arr):
    cont = 0
    
    if sum(arr) == 0:
        return 0    
    
    for x in arr:
        cont += 1
        if sum(arr[:cont+1]) == sum((arr[cont:])):
            return cont
    
    
        

print(find_even_index([20,10,-80,10,10,15,35]))