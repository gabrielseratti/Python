def twos_difference(lst): 
    arr = []
    lst.sort()
    for x in lst:
        for y in lst:
            if x-y == 2:
                arr.append((y, x))
    
    return arr

print(twos_difference([1, 2, 3, 4]))