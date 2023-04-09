def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count +=i
    return count


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    

def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance = mpg * fuel_left
    if distance >= distance_to_pump:
        return True
    else:
        return False
    

def solution(number):
    if number < 0:
        return 0
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 ==0:
            sum +=i 
    return sum


def reverse_list(l):
    return l[::-1]


def reverse(st):
    w = st.strip().split()
    w.reverse()
    return " ".join(w)

def number_to_string(num):
    return str(num)


def filter_words(st):
    a = st.split()
    b = " ".join(a)
    c = b.capitalize()
    return c


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def multiply(a, b):
    return a * b