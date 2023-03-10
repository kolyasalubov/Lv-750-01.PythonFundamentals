# Write a function that calculates the number of characters included in given string
# input: "hello"
# output: {"h":1, "e":1, "l":2,"o":1}

def char_count(str):
    count = {}
    for x in str:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    return count