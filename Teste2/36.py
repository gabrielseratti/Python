def points(games):
    points = 0
    for x in games:
        print(x)
        if x[0] > x[2]:
            points += 3
            print(points)
        if x[0] == x[2]:
            points += 1
            print(points)
        
    return points
    

print(points(["3:1", "2:2", "0:1","3:1", "2:2", "0:1","3:1", "2:2", "0:1"]))