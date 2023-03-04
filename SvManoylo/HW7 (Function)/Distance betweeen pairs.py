# import math
# def distance(x1, y1, x2, y2):
#     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#     return round(distance, 2)

def filter_words(st):
    st = str(st.capitalize())
    new_str = st.split() 
    print(' '.join(new_str))

st = "WOW this is REALLY          amazing"
x = filter_words(st)
print (x)
