def make_negative( number ):
    if number < 0:
        pass;
    else:
        number -= 2*number;
    return number

print(make_negative(-1))