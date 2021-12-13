from Finalproject.Methods import Addition
from Finalproject.Methods import Subtraction
from Finalproject.Methods import Multiplication
from Finalproject.Methods import Division

class Equation: 

    def __init__(self,input):
        self.input = input

    def set_Take_Apart(self):
        full = self.input
        value = full.split()
        self.value = value
        if value[1] == "+":
            self.type = Addition(self.value)
            self.answer = self.type.calculate()
            self.answer = str(self.answer)
        if value[1] == "-":
            self.type = Subtraction(self.value)
            self.answer = self.type.calculate()
            self.answer = str(self.answer)
        if value[1] == "*":
            self.type = Multiplication(self.value)
            self.answer = self.type.calculate()
            self.answer = str(self.answer)
        if value[1] == "/":
            self.type = Division(self.value)
            self.answer = self.type.calculate()
            self.answer = str(self.answer)
        self._store = self.value[0] + " " + self.value[1] + " " + self.value[2] + " = " + self.answer
    
    def get_Take_Apart(self):
        return self._store
