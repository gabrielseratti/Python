def uniq(seq): 
    i = 0
    while i < len(seq)-1:
        if seq[i] == seq[i+1]:
            seq.pop(i+1)
        else:
            i += 1
    return seq
    

print(uniq([]))