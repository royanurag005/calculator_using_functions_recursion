#Calculator
#addition
from art import logo
from replit import clear
def add(a,b):
    return a+b
#subtraction
def sub(a,b):
    return a-b
#multiplication
def multiply(a,b):
    return a*b
#division
def divide(a,b):
    return a/b
#dictionary
operations={
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" :divide,
}
def calculation():
    print(logo)
    n1=float(input("What's the first number ? : "))
    should_continue=True
    while should_continue:
        for operation in operations:
            print(operation)
        operation_symbol=input("Pick any operation from the line above : ")
        n2=float(input("What's the next number ? : "))
        operation_chosen=operations[operation_symbol]
        result=operation_chosen(n1,n2)
        print(f"{n1} {operation_symbol} {n2} : {result} ")
        rather_continue=input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if(rather_continue=='n'):
            should_continue=False
            calculation()
        elif(rather_continue=='y'):
            n1=result
            clear()
    # print("Thank You")
calculation()
