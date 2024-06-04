def hofstadter_q(n):
    q = []
    z = 0
    for x in range(1, n+1):
        if x <= 2:
            z = 1
            q.append(z)
        else:
            z = q[x-q[x-2]-1]+q[x-q[x-3]-1]
            q.append(z)
    return q[-1]

print(hofstadter_q(9))