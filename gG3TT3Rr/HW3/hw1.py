philosophy = """ 'Python's philosophy is based on the idea that there should be only one way to do something, and that way should be clear and easy to understand. '
'Better to be explicit than implicit. Never be ambiguous. '
'There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. '
'Now is better than never. Although never is often better than right now. '
'If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.' """

philosophy_upper = philosophy.upper()
better_count = philosophy.count("better")
never_count = philosophy.count("never")
is_count = philosophy.count("is")

philosophy_replace = philosophy_upper.replace("I", "&")

print("Philosophy in uppercase:\n", philosophy_upper)
print("\nNumber of occurrences of 'better':", better_count)
print("Number of occurrences of 'never':", never_count)
print("Number of occurrences of 'is':", is_count)

print("\nPhilosophy with I replaced with &: \n", philosophy_replace)