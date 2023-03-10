import math
def distance(x1, y1, x2, y2):
    """Distance function"""
    return round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)

print(distance.__doc__)
print(distance(1,1,0,0))