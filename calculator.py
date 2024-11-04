#program to  make a simple calculator
def mycal():
    num1 = int(input("enter 1ST number:- "))
    num2 = int(input("enter 2nd number:- "))
    choice = input("enter the choice,add,sub,mul,div:- ")
    if choice == "add":
        print("addition=", num1 + num2)
    elif choice == "sub":
        print("subtraction=", num1 - num2)
    elif choice == "mul":
        print("multiplication =", num1 * num2)
    elif choice == "div":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Division = ", num1 / num2)
    else:
        print("invalid choice")
mycal()