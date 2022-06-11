# self keyword is mandatory for calling variables into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object


class Calculator:
    num = 100  # class variable

    def __init__(self, a, b):  # default constructor
        self.firstnum = a
        self.secondnum = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def SumData(self):
        return self.firstnum + self.secondnum + self.num


obj = Calculator(2, 3)
obj.getData()
print(obj.SumData())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.SumData())
