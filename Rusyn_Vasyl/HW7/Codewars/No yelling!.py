def filter_words(st):
    s = st.strip()
    s = s.capitalize()
    
    while "  " in s:
        s = s.replace("  ", " ")
    return s