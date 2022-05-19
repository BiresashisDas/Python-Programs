# Author :- Biresashis Das

def add(n1, n2):
    return  n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : substract,
    "*" : multiplication,
    "/" : division
}
def calculator():
    f_num = float(input("What is the first number : "))
    for symbol in operation:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from above. ")
        s_num = float(input("What is the next number : "))
        new_operation = operation[operation_symbol]
        f_calculation = new_operation(f_num, s_num)

        print(f"{f_num} {operation_symbol} {s_num} = ", f_calculation)


        result = input(f"Type 'y' to calculating with {f_calculation} or type 'n' to start new calculation or s to stop.")

        if result == "y":
            f_num = f_calculation
        elif result == "n":
            should_continue = False
            calculator()
        elif result == "s":
            should_continue = False
            print("The program is stopped.")

calculator()




#         SAMPLE OUTPUT

#         What is the first number : 5
#         +
#         -
#         *
#         /
#         Pick an operation from above. *
#         What is the next number : 2
#         5.0 * 2.0 =  10.0
#         Type 'y' to calculating with 10.0 or type 'n' to start new calculation or s to stop.y
#         Pick an operation from above. +
#         What is the next number : 5
#         10.0 + 5.0 =  15.0
#         Type 'y' to calculating with 15.0 or type 'n' to start new calculation or s to stop.




