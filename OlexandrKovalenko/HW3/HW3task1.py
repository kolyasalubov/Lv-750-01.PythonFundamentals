rule = 'Although never is often better than *right* now'
search1 = rule.find('better')
search2 = rule.find('never')
search3 = rule.find('is')
letters = rule.upper()
replacing = rule.replace('i','&')
print(f"better {search1}, never {search2}, is {search3}")
print(letters, replacing, sep='\n')