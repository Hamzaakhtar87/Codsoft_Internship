def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("Please Select one option:")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Please Enter operation you want to perform (1/2/3/4): ")
    if choice > "4":
        print(f"Invalid Choice!, Please Enter (1/2/3/4)\n")
        continue

    num1 = float(input("\nPlease Enter your First Number: "))
    num2 = float(input("Please Enter your Second Number: "))

    if choice == "1":
        print("\n", num1, "+", num2, "=", add(num1, num2), "\n")
    elif choice == "2":
        print(num1, "-", num2, "=", sub(num1, num2), "\n")
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2), "\n")
    elif choice == "4":
        try:
            print(num1, "/", num2, "=", divide(num1, num2), "\n")
        except ValueError as e:
            print("Error:", e)
    # elif choice > "4":
    #     print("Invalid Choice!")
    #     break
