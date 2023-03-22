def func(**kwargs):
    print(kwargs)
    return kwargs

w = "hello"
h=w.count("h")
e=w.count("e")
l=w.count("l")
o=w.count("o")
    
w = func(h = h, e = e, l = l, o = o)
