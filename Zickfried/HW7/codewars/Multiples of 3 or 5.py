def solution(number):
    if number < 0:
        return 0
    
    
    multiples = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(set(multiples)) 