from math import sqrt
from point import Point

def calculate_distance(p1, p2):
    x = abs(p1.get_x() - p2.get_x())
    y = abs(p1.get_y() - p2.get_y())

    return sqrt(x**2 + y**2)

f_p_coords = input().split()
s_p_coords = input().split()

p1 = Point(float(f_p_coords[0]), float(f_p_coords[1]))
p2 = Point(float(s_p_coords[0]), float(s_p_coords[1]))

print(f'{calculate_distance(p1, p2):.3f}')