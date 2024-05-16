def opposite(number):
    if number < 0: 
       number += 2*(-number);
    else:
        number -= number *2;
    return number;

print(opposite(-1))