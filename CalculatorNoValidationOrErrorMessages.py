def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations =    {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

#print(operations["*"](4,8))   testing code so far

def calculator():
    continue_calc=True
    num1=float(input("enter first number:\n"))
    while continue_calc:

        [print(keys) for keys in operations.keys()]
        operator=(input("pick an operation:\n"))
        num2=float(input("enter second number:\n"))

        init_result=operations[operator](num1, num2)
        print(f"{num1} {operator} {num2}  = {init_result}")
        proceed=input(f"To continue working with {init_result} type 'y'.  To start a new calculation type 'n'.\n")

        if proceed =="y":
            num1 = init_result
        else:
            continue_calc=False
            print("\n" * 20) #gap if new calculation chosen
            calculator()

calculator()

