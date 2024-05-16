def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
print(high_and_low("1 2 3 4 5"))