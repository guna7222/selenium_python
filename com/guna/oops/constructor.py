# Constructor
class Name:
    class_variable = 100  # class variable

    # constructor
    def __init__(self, a, b):
        print("i will execute automatically after creating a object")
        self.num1 = a
        self.num2 = b

    def Hello(self):
        print("Hello, Guna")

    def addition(self):
        return self.num1 + self.num2
    # creating object for class


obj1 = Name(10, 22)
obj1.addition()
