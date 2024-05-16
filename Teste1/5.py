def likes(names):
    array_names = names.split(' ')
    if len(array_names) == 0:
        return 'no one likes this'
    elif len(array_names) == 1:
        return 'no one likes this'    
    elif len(array_names) == 2:
        return f'{array_names[0]} and {array_names[1]} like this'    
    elif len(array_names) == 3:
        return f'{array_names[0]}, {array_names[1]} and {array_names[2]} like this'    
    elif len(array_names) == 4:
        return f'{array_names[0]}, {array_names[1]} and {len(array_names)-2} others like this'    
    return array_names

print(likes('String'))git remote add origin https://github.com/gabrielseratti/Python