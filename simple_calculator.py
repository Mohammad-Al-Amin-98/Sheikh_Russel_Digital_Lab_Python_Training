# Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

#Function to find the remainder

def modulo(num1, num2):
    return num1%num2
while(True): 
    print("Please select an option -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Get Remainder")
    print("6. I don't want to continue!") 
    print()

# Take input from the user
    select = int(input("Select operations form 1, 2, 3, 4, 5, 6 :"))
    if select == 6:
        break
     
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print()
     
    if select == 1:
        print(number_1, "+", number_2, "=", add(number_1, number_2))
        print()
     
    elif select == 2:
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
        print()
     
    elif select == 3:
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
        print()
     
    elif select == 4:
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
        print()

    elif select == 5:
        print(number_1, "%", number_2, "=", modulo(number_1, number_2))
        print()

    else:
        print("Invalid input")
        print()
