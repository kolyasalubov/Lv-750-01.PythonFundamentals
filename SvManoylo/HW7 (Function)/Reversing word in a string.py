def reverse(st):
    st = st.strip().split()
    reverse_set = st[::-1]
    reverse_string = ' '.join(reverse_set)
    return str(reverse_string)