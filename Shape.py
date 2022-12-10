import math

def circle_area(r):
    Carea = f'{3.14 * (math.pow(r,2)):.2f}'
    return Carea

def rectangle_area(l,w):
    Rarea = f'{(l * w):.2f}'
    return Rarea

def square_area(s):
    Sarea = f'{math.pow(s,2):.2f}'
    return Sarea

def triangle_area(h,b):
    Tarea = f'{((h * b) / 2):.2f}'
    return Tarea

def circle_perimeter(r):
    Cperimeter = f'{(2 * 3.14 * r):.2f}'
    return Cperimeter

def rectangle_perimeter(l,w):
    Rperimeter = f'{2*(l + w):.2f}'
    return Rperimeter

def square_perimeter(s):
    Sperimeter = f'{(4 * s):.2f}'
    return Sperimeter

def triangle_perimeter(a,b,c):
    Tperimeter = f'{(a + b + c):.2f}'
    return Tperimeter

