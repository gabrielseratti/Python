def warn_the_sheep(queue):
    y = 0
    for x in queue:
        if x == 'wolf' and queue[len(queue)-1] != 'wolf':
            return f'Oi! Sheep number {len(queue)-(y+1)}! You are about to be eaten by a wolf!'
        if queue[len(queue)-1] == 'wolf':
            return "Pls go away and stop eating my sheep"
        y += 1
        # y += 1
        # elif:
        # len = 5 // pos = 3 // posove = 3 + 1
    # return

print(warn_the_sheep(["sheep", "wolf", "sheep", "sheep", "sheep"]))