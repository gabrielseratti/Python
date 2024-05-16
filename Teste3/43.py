import math

def nearest_sq(n):
        if isinstance(round(math.sqrt(n)), int):
            return n
        else:
            z, w = 0, 0
            for x in range(100):
                if isinstance(round(math.sqrt(n)), int):
                    return n
                else:
                    n+1
            for y in range(100):
                if isinstance(round(math.sqrt(n)), int):
                    return n
                else:
                    n-1
            return z,y


print(nearest_sq(122))