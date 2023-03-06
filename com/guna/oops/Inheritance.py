from com.guna.oops.constructor import Name


# Inheritance

class Inheritance(Name):
    num2 = 200

    # child constructor
    def __init__(self):
        Name.__init__(self, 1, 22)

    def get_complete_data(self):
        return self.num1 + Inheritance.num2 + self.addition()


obj1 = Inheritance()
print(obj1.get_complete_data())
