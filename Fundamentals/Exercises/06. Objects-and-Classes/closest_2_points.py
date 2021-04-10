from point import Point
from sys import maxsize
from math import sqrt

def calculate_distance(p1, p2):
    x = abs(p1.get_x() - p2.get_x())
    y = abs(p1.get_y() - p2.get_y())
    return sqrt(x**2 + y**2)

n = int(input())
points = []

for _ in range(n):
    data = list(map(float, input().split()))
    points.append(Point(data[0], data[1]))

min_distance = maxsize
s_p1, s_p2 = None, None

for i in range(n - 1):
    for j in range(i + 1, n):
        distance = calculate_distance(points[i], points[j])
        if min_distance > distance:
            min_distance = distance
            s_p1 = points[i]
            s_p2 = points[j]

print(f'{min_distance:.3f}')
print(f'({s_p1.get_x():g}, {s_p1.get_y():g})')
print(f'({s_p2.get_x():g}, {s_p2.get_y():g})')