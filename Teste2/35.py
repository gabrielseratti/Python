def elevator(left, right, call):
    if abs(call-right >= call - left):
        return 'right'
    elif abs(call-left > call - right):
        return 'left'
    


print(elevator(1, 0, 2))