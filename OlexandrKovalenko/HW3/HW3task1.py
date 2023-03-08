rule = 'Although never is often better than *right* now'
search1 = rule.count('better')
search2 = rule.count('never')
search3 = rule.count('is')
letters = rule.upper()
replacing = rule.replace('i','&')
print(f"better {search1}, never {search2}, is {search3}")
print(letters, replacing, sep='\n')
