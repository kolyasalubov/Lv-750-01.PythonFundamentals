# def mean(number):
#     a = len(str(number))
#     b = list(str(number))
#     c = 0
#     for i in b:
#         i = int(i)
#         c += i
#
#
#     return  round(c/a)
#
# print(mean(512))


# def integer_boolean(binary_number):
#     a = str(binary_number)
#     list1 = []
#     for i in a :
#         if i == "0":
#             list1.append(False)
#         else:
#             list1.append(True)
#     return list1
#
# print(integer_boolean(100101))



def count_vowels(word):
    count = 0
    word = word.lower()
    for i in range(len(word)):
        a = [i]
        if word[i] in ['a','o','e','y','u','i']:
            count += 1
    return count

print(count_vowels("IIIIiiiiiiiii"))