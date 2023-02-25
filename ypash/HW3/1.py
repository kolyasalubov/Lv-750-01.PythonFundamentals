count_better = 0
count_never = 0
count_is = 0
pythonPhilosophy = ("Beautiful is better than ugly.\
                    Explicit is better than implicit.\
                    Simple is better than complex.\
                    Complex is better than complicated.\
                    Flat is better than nested.\
                    Sparse is better than dense.\
                    Readability counts.\
                    Special cases aren't special enough to break the rules.\
                    Although practicality beats purity.\
                    Errors should never pass silently.\
                    Unless explicitly silenced.\
                    In the face of ambiguity, refuse the temptation to guess.\
                    There should be one-- and preferably only one --obvious way to do it.\
                    Although that way may not be obvious at first unless you're Dutch.\
                    Now is better than never.\
                    Although never is often better than *right* now.\
                    If the implementation is hard to explain, it's a bad idea.\
                    If the implementation is easy to explain, it may be a good idea.\
                    Namespaces are one honking great idea -- let's do more of those!")


print("First task:")
sub1 = "better"
sub2 = "never"
sub3 = "is"
print(f"better = {pythonPhilosophy.count(sub1)} times")
print(f"never = {pythonPhilosophy.count(sub2)} times")
print(f"is = {pythonPhilosophy.count(sub3)} times")

print("Second task:")
print(pythonPhilosophy.upper())

print("Third task:")
print(pythonPhilosophy.replace("is", "&"))
