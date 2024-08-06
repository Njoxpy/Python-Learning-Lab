# define function for performing arithmetic operation
# This is the module I will import into the app.py
def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("Cannot divide by zero!")


def help():
    print("""Enter first number then second number, 
    then choose the operation type you want
    """)


# welcome user
print("Welcome to Mdudu calculator. \n")

# allow user to enter first number and second number
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("This is the basic calculator for performing arithmetic operation, Enter the number of the operation.")
print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Help""")

operation_type = int(input("Enter operation number: "))
match operation_type:
    case 1:
        result = addition(number1, number2)
        print(f"Result after addition =  {result}")
    case 2:
        result = subtraction(number1, number2)
        print(f"Result after subtraction =  {result}")
    case 3:
        result = multiplication(number1, number2)
        print(f"Result after multiplication =  {result}")
    case 4:
        result = division(number1, number2)
        print(f"Result after division =  {result}")
    case 5:
        help()
    case _:
        print("Wrong operation type")
