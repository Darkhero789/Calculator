from Finalproject.Equation import Equation

#This project needs to demonstrate the 4 principles of object oriented programming. principle(s) left are Inheritance

class calculator:

    # A code template meant to control everything so that a person can input numbers and certain symbols so that a equation is created and then the answer is provided.

    def Introduction(self):
        print("Welcome to the python basic calculator. With this calculator you can do basic math with ease. Simply input the numbers and choose what type of equation and the calculator will give you the answer.")

    def gather(self):
        self.Input = input("Please enter the equation and put spaces between the numbers(ex: 1 + 2, 4 * 3): ")

    def set_equation(self):
        self._Equation = Equation(self.Input)
        self._Equation.set_Take_Apart()
        self._end = self._Equation.get_Take_Apart().split()

    def get_equation(self):
        print(f"The answer to your equation is {self._end[4]}")

