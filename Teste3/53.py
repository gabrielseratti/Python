def find_outlier(integers):
    a = sorted(integers, key=lambda x: x%2==0)
    if a[0]%2!=0 and a[1]%2!=0:
        return a[len(a)-1]
    else:
        return a[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))