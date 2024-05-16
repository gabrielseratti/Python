def find_smallest_int(arr):
    s = arr[0]
    for x in arr:
        if x < s:
            s = x
        else:
            pass
    return s

print(find_smallest_int([34, -345, 1, 10]))