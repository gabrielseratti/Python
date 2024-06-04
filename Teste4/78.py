import math

def area_of_inscribed_polygon(circle_radius, number_of_sides):
    angulo = (360/number_of_sides)/2
    cat_oposto = (math.sin(math.radians(angulo)))*circle_radius
    cat_adjacente = (math.cos(math.radians(angulo)))*circle_radius
    area_triangulo = cat_oposto * cat_adjacente/2
    area_total = area_triangulo*2*number_of_sides
    
    return area_total


print(area_of_inscribed_polygon(4, 5))