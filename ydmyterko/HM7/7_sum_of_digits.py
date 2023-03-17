def solution(number):
    """Sum of digits multiples 3 or 5"""
    sum=0
    for digit in range(number):
        if digit%3==0 or digit%5==0:
            sum += digit

    return sum

print(solution(10))
  