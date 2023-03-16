def reverse(st):
s = st.strip()
words = s.split()
words_reversed = words[::-1]
s_reversed = " ".join(words_reversed)
return s_reversed