def string(string:str) -> None:
    word=string
    lettet_count={}
    for letter in word:
        if letter in lettet_count:
            lettet_count[letter] += 1
        else:
            lettet_count[letter] = 1
    print(f"the word{word} і букв в ньому {lettet_count}")
string("hello")
    

    








