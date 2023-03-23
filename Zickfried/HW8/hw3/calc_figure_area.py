from math import (pi,
                  pow
                  )

def rectandle_area(a, b):
    '''
    Calculate area of rectandle
    '''
    return a * b


def triangle_area(base, high):
    '''
    Calculate area of triangle
    '''
    return 0.5 * base * high


def circle_area(radius):
    '''
    Calculate area of circle
    '''
    
    return pi * pow(radius, 2)