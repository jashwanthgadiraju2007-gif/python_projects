import math
def calculator(a, b, choice):
    if choice == "+":
        return a + b
    elif choice == "-":
        return a - b
    elif choice == "*":
        return a * b
    elif choice == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    elif choice == "%":
        return a % b
    elif choice == "sq":
        return math.sqrt(a)
    elif choice == "!":
        return math.factorial(a)
    elif choice == "^":
        return math.pow(a,b)
    else:
        return "Invalid operator"


def main():
    while True:
        print("\nOperations: +  -  *  /  %  sq  ! ^  exit")
        choice = input("Choose an operation: ")

        if choice == "exit":
            print("Calculator closed.")
            break
        if choice in ["sq", "!"]:
            a = int(input("Enter a number: "))
            b = None
        else:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
        print("Result:", calculator(a, b, choice))
main()
