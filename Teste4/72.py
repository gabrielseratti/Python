import math

def candles(m, n):
    # if m <= 1 or m >= 50 or n < 2 or n >= 5:
    #     return
    candles = m
    candles_burnt = 0
    leftovers = 0
    while candles != 0 or leftovers != 1:
        if candles >= 1:
            candles_burnt += candles
            leftovers += candles
            candles = 0
        if leftovers % n != 0 and leftovers != 1:
            if leftovers < n:
                break
            else:
                candles += math.floor(leftovers / n)
                leftovers = leftovers % n
        elif leftovers % n == 0:
            candles += leftovers / n
            leftovers = 0
    return int(candles_burnt)   
print(candles(18, 3))