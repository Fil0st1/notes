
import math

#! Problem 1 (solved)


class programmer:
    name = ""
    salary = 100000
    language = "Python"
    def __init__(self, a, b, c):
        self.name = a
        self.salary = b 
        self.language = c 
        print(f"Hello {a} your language is {c} and your salary is {b}")

a = input("What is your name: ")
b = int(input("What is you salary: "))
c = input("What is your language of expertise: ")

a = programmer(a, b, c)

#* ============================================================================

#! Problem 2 (solved)

# class Calculator:
#     @staticmethod
#     def greet():
#         print("Hello user!")
#     def __init__(self, a):
#         self.a = a
#     def square(self):
#         print(f"The square of {self.a} is {self.a * self.a}")
#     def cube(self):
#         print(f"The cube of {self.a} is {self.a * self.a * self.a}")
#     def square_root(self):
#         print(f"The square root of {self.a} is {math.sqrt(self.a) }")



# a = int(input("What is first number? "))
# Calculation = Calculator(a)
# Calculation.greet()

# Calculation.square()
# Calculation.cube()
# Calculation.square_root()

#* ============================================================================

#! Problem 3


        