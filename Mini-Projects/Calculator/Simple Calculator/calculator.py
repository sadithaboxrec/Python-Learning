def display():
    print("Hello, Welcome to the Calculator")
    print("What do you like to do?")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def aftermath():

    while True:
        cal_after=input("Enter N to quit and Enter Y to another calculation:").upper()

        if cal_after == "N":
            print("Thank you for using Calculator")
            exit()
        elif cal_after == "Y":
            # display()
            main()
        else:
            print("Please enter a correct letter.")



def get_operator():
    operator_choice = ["1", "2", "3", "4"]

    while True:
        operator = input("Enter your choice: ")

        if operator not in operator_choice:
            print("Invalid choice. Please try again.")
            continue
        else:
            return int(operator)

def get_input(operator):

    while True:

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if operator == 4 and number2 == 0:
                print("You can't divide a number by 0, add again plz")
                continue

            return number1, number2

        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_cal(number1, number2,operator):
    if operator == 1:
        return number1 + number2
    elif operator == 2:
        return number1 - number2
    elif operator == 3:
        return number1 * number2
    elif operator == 4:
        return number1 / number2

def main():
    display()
    operator=get_operator()
    number1 ,number2=get_input(operator)
    result = get_cal(number1, number2,operator)

    print(f"\n\nThe Result is {result}")

    aftermath()


if __name__ == '__main__':
    main()

