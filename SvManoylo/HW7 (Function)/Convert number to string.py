# def number_to_string(num):
#     num_str = str(num)
#     return num_str
def reverse(st):
    st = st.strip().split()
    reverse_set = st[::-1]
    reverse_string = ' '.join(reverse_set)
    return str(reverse_string)



st = "World Hello"
x = reverse(st)
print(x)