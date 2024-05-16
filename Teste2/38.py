def twice_as_old(dad_years_old, son_years_old):
    years = 0
    if dad_years_old < son_years_old*2:
        for x in range(1000):
            years -= 1
            dad_years_old -= 1
            son_years_old -= 1
            if dad_years_old == son_years_old*2:
                return abs(years)
    if dad_years_old > son_years_old*2:
        for x in range(1000):
            years += 1
            dad_years_old += 1
            son_years_old += 1
            if dad_years_old == son_years_old*2:
                return abs(years)
    else:
        return 0

print(twice_as_old(58, 29))