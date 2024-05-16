def how_many_step(a, b):
    if 0 < a <= b:
        for x in range(b):
            
            if a == b:
                return count
            elif (a*2 <= b):
                a *= 2
                count += 1
            else:
                a += 1
                count += 1
    else:
        return a


print(how_many_step(1, 10))