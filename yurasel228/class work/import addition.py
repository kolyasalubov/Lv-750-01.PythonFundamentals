import addition

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = addition.add(num1, num2)
    elif choice == '2':
        result = addition.subtract(num1, num2)
    elif choice == '3':
        result = addition.multiply(num1, num2)
    elif choice == '4':
        result = addition.divide(num1, num2)
    else:
        print("Invalid input")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()