def merge_arrays(arr1 = [], arr2 = []):
    arr1, arr2 = set(arr1), set(arr2)
    arr1, arr2 = list(arr1), list(arr2)
    for item in arr2:
        if item not in arr1:
            arr1.append(item)
    arr1.sort()

    return arr1

print(merge_arrays([1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12]))