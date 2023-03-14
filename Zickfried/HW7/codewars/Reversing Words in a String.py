def reverse(st):
    s = st.split()[::-1]
    my_list = []
    for i in s:
       my_list.append(i) 
    return " ".join(my_list)