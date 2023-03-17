def solution(number):
    counter=0
    for i in range (0,number):
        if i%3==0 or i%5==0:
            if i<number:
                counter=counter+i
    return counter
 