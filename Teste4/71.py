def apple_boxes(k):
    even = 1
    odds = 1
    for x in range(1, k+1):
        if x % 2 == 0:
            even += x*x
        else:
            odds += x*x
    return even - odds

print(apple_boxes(5))