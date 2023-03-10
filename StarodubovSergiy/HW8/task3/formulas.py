import math

def rectangle(a,b):
    rectangle_area = a*b
    return rectangle_area

def triangle(base,h):
    triangle_area = 0.5*base*h
    return triangle_area

def circle(r):
    circle_area = math.pi*math.pow(r,2)
    return circle_area