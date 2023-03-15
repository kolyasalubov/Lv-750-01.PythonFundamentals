def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)