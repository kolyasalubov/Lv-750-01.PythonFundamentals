def lettuce_decorator(func):
    def wrapper():
        print("<\\ ^^^^^^^ />")
        func()
    return wrapper

def tomato_decorator(func):
    def wrapper():
        func()
        print("# tomato #")
    return wrapper

def meat_decorator(func):
    def wrapper():
        print("– meat–")
        func()
    return wrapper

def salad_decorator(func):
    def wrapper():
        print("~ salad ~")
        func()
        print("<\\ ______ />")
    return wrapper

@lettuce_decorator
@tomato_decorator
@meat_decorator
@salad_decorator
def make_sandwich():
    pass

make_sandwich()