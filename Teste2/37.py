def pillars(num_pill, dist, width):
    if num_pill < 1 or dist < 10 or dist > 30 or width < 0.10 or width > 0.50:
        return
    else:
        distance = (num_pill-2)*(dist+width)+2*width+dist
        return distance


print(pillars(2, 10, 0.5))