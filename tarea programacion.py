import math

def area_lateral_vagon(a, b, r):
    area_rectangulo = a * b
    area_rueda = math.pi * r ** 2
    area_total = area_rectangulo + 2 * area_rueda
    return area_total

print(area_lateral_vagon(2, 5, 0.5))

