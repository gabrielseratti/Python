def flip(d, a):
    if d == 'R':
        a.sort(reverse=False)
        return a
    if d == 'L':
        a.sort(reverse=True)
        return a

print(flip('L', [1, 4, 5, 3, 5 ]))