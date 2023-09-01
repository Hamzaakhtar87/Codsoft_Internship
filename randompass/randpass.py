import random
import string

while True:
    user_input = input("Please Enter the lenght for the password or \"quit\" to close the program: ")

    if user_input.lower() == "quit":
        print("\nProgram Closed!\n")
        break

    try:
        lenght = int(user_input)

        if lenght <= 0:
            print("\nInvalid Input!, Please Enter a positive Number for lenght\n")
            continue

        def pass_generate(lenght):
            chr = string.ascii_letters + string.digits + string.punctuation

            password = ""
            for i in range(lenght):
                password += random.choice(chr)
            return password
        generated_pass = pass_generate(lenght)
        print("\nYour Password is: ", generated_pass, "\n")

    except ValueError:
        print("Invalid input!\nPlease Enter a Valid Lenght")