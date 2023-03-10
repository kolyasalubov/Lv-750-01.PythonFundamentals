file = open("./Zen.txt", "r")
data = file.read()
occurance_1=data.count("better")
occurance_2=data.count("never")
occurance_3=data.count("is")
print("Number of occurences of the word better : ", occurance_1)
print("Number of occurences of the word never : ", occurance_2)
print("Number of occurences of the word is : ", occurance_3)

capital_data = data.upper()
print("Capital text starts here: ")
print(capital_data)

replace_data = data.replace("i", "&")
print("Modify text starts here:")
print(replace_data)

