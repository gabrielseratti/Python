def max_wedding_cost(C, r, S, T, W):
    savings = (C*((1 + r) ** (T)))
    formatado = format(savings, '.2f')

    

    
    
    
    return formatado


print(max_wedding_cost(1000, 0.05, 3000000, 35, 5))