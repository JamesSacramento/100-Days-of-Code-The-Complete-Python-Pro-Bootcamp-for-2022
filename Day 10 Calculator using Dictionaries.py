import os
clear = lambda: os.system('cls')


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
#Calculator

#add function
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1 - n2
#multiply
def multiply(n1, n2):
  return n1 * n2
#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}
def calculatorFunction():
    print(logo)
    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)

    continueCalc = True

    while continueCalc:
        operation_symbol = input("Pick an operation? ")
        num2 = float(input("What's the next number? "))
        calculation_f = operations[operation_symbol]
        answer = calculation_f(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type \"y\" to continue calculating with {answer}, or type \"n\" to start new calc.: ") == "y":
            num1 = answer
        else:
            continueCalc = False
            clear()
            calculatorFunction()
            

calculatorFunction()




            


