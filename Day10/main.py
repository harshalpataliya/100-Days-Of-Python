import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    should_continue = True
    number1 = float(input("Please enter your first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Please enter your operation: ")
        number2 = float(input("Please enter your second number: "))
        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            number1 = answer
        else:
            should_continue = False
            print("\n" * 55)
            calculator()

calculator()