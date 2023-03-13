def area_triange():
    a = int(input('Please input a'))
    b = int(input('Please input b'))
    c = int(input('Please input c'))
    print(1/4 * ((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c))**(1/2))


def area_rectangle():
    a = int(input('Please input a'))
    b = int(input('Please input b'))
    print(a*b)

def area_circle():
    Radius = int(input('Please input Radius'))
    Pi = 3.14159
    print(Pi*(Radius**2))

def default():
   print("Bye!")


def main(value):
    match value:
        case 'T':
            area_triange()
        case 'R':
            area_rectangle()
        case 'C':
            area_circle()
        case '_':
            default()


start = 1
while start :
    choose = input('Please choose your figure for taking the area\n'
                   'if you want to take area of circle, input "C"\n'
                   'if it might be a triangle input "T"\n'
                   'to find the area of rectangle - "R"\n'
                   'for finish input something else')
    if choose != 'T' and choose != 'R' and choose != 'C':
        choose = '_'
        main(choose)
        break
    main(choose)
