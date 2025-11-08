class Calculator:
    def add(self, a, b):
        sum = a + b
        print(f"The sum is {sum}")
    def subtract(self, a, b):
        result = a - b
        print(f"The deffrence is {result}")
    def multiply(self, a, b):
        product = a * b
        print(f"The product is {product}")
    def divide(self, a, b):
        try:
            quotient = a / b
            print(f"The qoutient is {quotient}")
        except ZeroDivisionError:
            print("You can't divide by zero")
calculator = Calculator()
calculator.add(2, 4)
calculator.subtract(15,10)
calculator.multiply(7,7)
calculator.divide(9,0)