def is_square(n):    
    if n >= 0:
        for x in range(n):
            if x*x == n:
                return True

    return False # fix me

print(is_square(0))
