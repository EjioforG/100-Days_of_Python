print("Welcome to Godswill's basic canculator")
def mycalc():
    num1 = int(input("Enter a number: "))
    op =  input("Enter an operator either +, -, * or /: ")
    num2 = int(input("Enter a second number: "))
    if op == "/":
        if num2 == 0:
            print("Invalid operation")
        else:
            print(num1/num2)

    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "+":
        print(num1 + num2)

    else:
        print("Wrong operation input, Try again")

mycalc()
done = False
calc2 = input("Do you wish to do another calculation? Yes or No: ").lower()
while calc2 == "yes":
    mycalc()
if calc2 == "no":
    done == True
    print("Thanks for using my calculator")



        



