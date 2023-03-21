def calculate_area():
    """
    Calculate area of a figure based on user input.

    Figures:
    1 - rectangle
    2 - triangle
    3 - circle
    """

    figur = int(input('Enter 1-3 to select which figure area to calculate (1 - rectangle, 2 - triangle, 3 - circle): '))
    match figur:
        case 1:
            print('Rectangle area:', (lambda side1, side2: side1 * side2)(
                float(input('Enter Side 1: ')),
                float(input('Enter Side 2: '))
            ))
        case 2:
            print('Triangle area:', (lambda base, height: 0.5 * base * height)(
                float(input('Enter base: ')),
                float(input('Enter height: '))
            ))
        case 3:
            print('Circle area:', (lambda radius: 3.14 * radius)(
                float(input('Enter radius: '))
            ))
        case _:
            print('Please enter 1, 2 or 3 to select a figure')


# help(calculate_area)
calculate_area()