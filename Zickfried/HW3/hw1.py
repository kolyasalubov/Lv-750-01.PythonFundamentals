#first task
pythPhilosophy = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""" 

key_words = ["better", "never", "is"]
word_counts = {}

for word in key_words:
    count = pythPhilosophy.count(word)
    word_counts[word] = count     

print(word_counts)

#second task

print(pythPhilosophy.upper())

#third task

print(pythPhilosophy.replace("i", "&"))
   
# ####another method
# print("In 'Zen of Python' the word \"better\" repeat", pythPhilosophy.count("better"), 'times')
# print("In 'Zen of Python' the word \"never\" repeat", pythPhilosophy.count("never"), 'times')
# print("In 'Zen of Python' the word \"is\" repeat", pythPhilosophy.count("is"), 'times')

# print(pythPhilosophy.upper())

# print(pythPhilosophy.replace("i","&"))         