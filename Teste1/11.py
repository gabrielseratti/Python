def positive_sum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum += x
        else:
            pass
    return sum

print(positive_sum([1,-4,7,12,11]))