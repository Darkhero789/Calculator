class Operator:
    def __init__(self,value):
        self.value = value
    
    def calculate(self):
        Num1 = self.value[0]
        Num1 = int(Num1)
        Num2 = self.value[2]
        Num2 = int(Num2)
       

class Addition(Operator):

    def calculate(self):
        Num1 = self.value[0]
        Num1 = int(Num1)
        Num2 = self.value[2]
        Num2 = int(Num2)
        self.add = Num1 + Num2
        return self.add

class Subtraction(Operator):

    def calculate(self):
        Num1 = self.value[0]
        Num1 = int(Num1)
        Num2 = self.value[2]
        Num2 = int(Num2)
        self.subtract = Num1 - Num2
        return self.subtract

class Multiplication(Operator):

    def calculate(self):
        Num1 = self.value[0]
        Num1 = int(Num1)
        Num2 = self.value[2]
        Num2 = int(Num2)
        self.multiply = Num1 * Num2
        return self.multiply

class Division(Operator):

    def calculate(self):
        Num1 = self.value[0]
        Num1 = int(Num1)
        Num2 = self.value[2]
        Num2 = int(Num2)
        self.divide = Num1 / Num2
        return self.divide