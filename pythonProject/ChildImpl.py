from Oops import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def finalSum(self):
        return self.num2 + self.num + self.SumData()


obj = ChildImpl()
print(obj.finalSum())
