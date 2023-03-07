# Solution #1
# def greet(name):
#     """Greet function"""
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)

# Solution #2
def greet(name):
    """Greet function"""
    return "Hello, {name}!".format(name=('my love' if name=="Jonny" else name))

print(greet.__doc__)
print(greet("Jonny"))