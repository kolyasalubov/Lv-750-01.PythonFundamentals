import addition

def main():
    print("Select operation:")
    print("1. Multiply")
    print("2. Divide")

    choice = input("Enter choice (1/2): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    if choice == '1':
        result = addition.multiply(num1, num2)
    elif choice == '2':
        result = addition.divide(num1, num2)
    else:
        print("Invalid input")


    print("Result:", result)

if __name__ == "__main__":
    main()