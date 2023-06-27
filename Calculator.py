previous_calculations = []
# Display the menu
def display_menu():
    print("\nSelect operation.\n")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $ ")
    print("9.History  : ?")



# Addition two numbers
def addition(first_num: float, secound_num: float) -> float:
    return first_num + secound_num


# subtraction two numbers
def subtraction(first_num: float, secound_num: float) -> float:
    return first_num - secound_num


# Multiplication two numbers
def multiplication(first_num: float, secound_num: float) -> float:
    return first_num * secound_num


# Division two numbers
def divition(first_num: float, secound_num: float) -> float | str:
    if secound_num == 0:
        print("float division by zero")
        return "None"
    else:
        return first_num / secound_num


# Exponentiation
def exponentiation(first_num: float, secound_num: float) -> float:
    return first_num ** secound_num


# Modulus
def modulus(first_num: float, secound_num: float) -> int:
    return first_num % secound_num



# Calculation print
def cal_print(operator: str) -> None | bool:
    while True:
        first_number = input("Enter first number: ")

        if first_number.endswith("$"):
            return True
        elif first_number.endswith("#"):
            return False
        secound_number = input("Enter second number: ")
        if secound_number.endswith("$"):
            return True
        elif secound_number.endswith("#"):
            return False

        try:
            num1 = float(first_number)
            num2 = float(secound_number)
        except ValueError:
            print("Not a number.Please try again.")
            continue

        if operator == "+":
            answer = addition(num1, num2)
        elif operator == "-":
            answer = subtraction(num1, num2)
        elif operator == "*":
            answer = multiplication(num1, num2)
        elif operator == "/":
            answer = divition(num1, num2)
        elif operator == "%":
            answer = modulus(num1, num2)
        elif operator == "^":
            answer = exponentiation(num1, num2)
        else:
            print("Something Went Wrong")
        print(f"\n{num1} {operator} {num2} = {answer}")
        previous_calculations.append(f"{num1} {operator} {num2} = {answer}")
        break

# show history
def history(histoty_list : list) ->None:
    if histoty_list == []:
        print("\nNo past calculations to show")
    else:
        print()
        for cal in histoty_list:
            print(cal)



while True:
    display_menu()
    user_choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    if user_choice == "+" or user_choice == "-" or user_choice == "*" or user_choice == "/" or user_choice == "^" or user_choice == "%":
        check = cal_print(user_choice)
        if check == True:
            continue
        elif check == False:
            print("\nDone. Terminating")
            break
    elif user_choice == "#":
        print("\nDone. Terminating")
        break
    elif user_choice == "?":
        history(previous_calculations)
    else:
        print("\nUnrecognized operation.")



