def correct_tail(body, tail):
    """Who's tail"""
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    else:
        return False
    
print(correct_tail("Fox", "x"))
