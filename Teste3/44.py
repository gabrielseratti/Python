def check_exam(arr1,arr2):
    count = 0
    for x, y in zip(arr1, arr2):
        print(x, y)
        if x == y:
            count += 4;
        if x != y and y != '':
            count -= 1
        else:
            pass
    if count < 0:
        return 0
    return count
  
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))