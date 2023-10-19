def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def main():
    try:
        user_input = int(input("Choose a decimal number:    "))
        conversion_choice = int(input("Choose conversion-\n1. Binary \n2. Hexadecimal \n3. Octal\n"))

        if conversion_choice == 1:
            result = decimal_to_binary(user_input)

        elif conversion_choice == 2:
            result = decimal_to_hexadecimal(user_input)

        elif conversion_choice == 3:
            result = decimal_to_octal(user_input)

        else:
                print('invalid')
                return

        print(f"The result is: {result}")

    except ValueError:
        print("Incorrect answer, please type in a compatible one.")

if __name__ == "__main__":
    main()
