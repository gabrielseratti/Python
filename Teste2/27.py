def flick_switch(lst):
    state = True
    # lista = []
    for x in lst:
        if x.lower() == 'flick':
            state = not state
            # lista.append(state)
            return state
        else:
            # lista.append(state)
            return state
    

print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))