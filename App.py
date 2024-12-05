import os
from time import *

operations = {
    "+": "Add",
    "-": "Subtract",
    "*": "Multiply",
    "/": "Divide",
    "!": "Exit"
}

def GetNumber():
    number = None

    while number == None:
        try:
            number = float(input("Enter the number\n : "))
        except Exception:
            print("Please enter a decimal number.")
    
    return number

def GetOperation():
    operation = None

    while operation == None:
        op = input("Enter the operation you want to perform next (+, -, *, /), or enter '!' to exit.\n : ")

        if op in operations:
            operation = op
    
    return operation

class Calculator:
    def __init__(self):
        self.Active = True
        self.Result = 0
        self.OperationStack = []
        
    
    def Start(self):
        while self.Active:
            os.system("cls")
            print(f"Current Result: {self.Result}")
            operation = GetOperation()

            if operation != "!":
                num = GetNumber()
                self.OperationStack.append((num, operation))
                functionName = operations[operation]
                func = getattr(self, functionName)

                func(num)
            else:
                self.Active = False
    
    def Add(self, value):
        self.Result += value

    def Subtract(self, value):
        self.Result -= value

    def Multiply(self, value):
        self.Result *= value
    
    def Divide(self, value):
        try:
            self.Result /= value
        except ZeroDivisionError:
            print("You cannot divide by zero! This operation was not performed.")
            sleep(3)

    def ShowSummary(self):
        os.system("cls")
        print("Your operation stack:")

        for i, value in enumerate(self.OperationStack):
            operator = value[1]
            operand = value[0]

            extension = ""

            if operator == "/" and operand == 0:
                extension = " (skipped due to 0 division attempt)"

            print(f"{i + 1}: {operator} {operand}{extension}")

        print()
        print(f"Your final result: {self.Result}")

calc = Calculator()
calc.Start()
calc.ShowSummary()