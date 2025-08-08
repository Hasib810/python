def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True

    v1 = float(input("enter a value: "))

    while should_continue: 

        for symbol in operators:
            print(symbol)

        operators_symbol = input("choose an operator: ")

        v2 = float(input("enter a value: "))

        answer = operators[operators_symbol](v1, v2)

        print(f"{v1} {operators_symbol} {v2} = {answer}")

        choice = input("type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            v1 = answer
        else:
            should_continue = False

            print("\n"*5)
            calculator()
calculator()