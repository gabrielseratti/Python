def array_diff(a, b):
    results = []
    for x in a:
        if x not in b:
            results.append(x)
    return results

print(array_diff([1,2,2,2,3],[2]))