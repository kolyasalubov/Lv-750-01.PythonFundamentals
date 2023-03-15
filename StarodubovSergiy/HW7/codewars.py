#I.
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#II.
import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    rounded_distance = round(dist, 2)

    return(rounded_distance)

#III.
def filter_words(st):
    if not st:
        return ""

    first_char = st[0]
    if not first_char.isalpha():
        st = st[1:]
    words = st.split()
    if words:
        words[0] = words[0].capitalize()
    output_string = " ".join(words)
    return output_string

#IV.
def number_to_string(num):
    num = str(num)
    return num

#V.
def reverse(st: str):
    words = st.strip().split()
    words.reverse()
    return " ".join(words)

#VI.
def reverse_list(l):
    return l[::-1]

#VII.
def solution(number):
    if number <0:
        return 0
    
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 ==0:
            result +=i
        
    return result

#VIII.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel = distance_to_pump / mpg
    return fuel_left >= fuel

#IX.
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    return name

#X.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
#XI.
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count +=i
    return count

#XII.
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False