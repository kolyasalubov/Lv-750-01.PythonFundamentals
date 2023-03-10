def reverse(st):
    """Reverse function"""
    return ' '.join(st.split()[::-1])

print(reverse.__doc__)
print(reverse("Hellow world"))