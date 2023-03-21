def reverse(st):
    string = st.split()[::-1]
    l = []
    for i in string:
        l.append(i)
    return " ".join(l)