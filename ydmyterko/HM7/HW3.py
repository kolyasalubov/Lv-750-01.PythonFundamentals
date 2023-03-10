def Number_of_characters(str) -> None:
    char_dict = {}
    for char in str:
        cnt = str.count(char)
        char_dict.update({char : cnt})
    print(char_dict)

str = input("Please enter a string: ")
Number_of_characters(str)