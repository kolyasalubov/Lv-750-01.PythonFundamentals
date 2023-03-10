from math import sqrt

def distance(x1, y1, x2, y2):
    """    Calculate the distance between two ordered pairs (x1, y1) and (x2, y2).
    Round the distance to two decimal places.

    Args:
        x1 (float): x-coordinate of the first point
        y1 (float): y-coordinate of the first point
        x2 (float): x-coordinate of the second point
        y2 (float): y-coordinate of the second point"""

    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)

print(distance(2, 4, 5, 10))