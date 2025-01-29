# class employee:
#     name =  "Aditya"
#     language = "py"
#     salary = 1200000

#! name, language, salary are an attribute

# Aditya = employee()       #! Aditya is an object
# Aditya.name = "Aditya Yadav"  #? This is an instance attribute
# print(Aditya.name, Aditya.language)

#? Here name is object attribute and salary and language are class attributes as they directly belong to the class


#* ===================================================================

#! Instance attribute >>>>> class attribute

#* ==================================================================

#! Self parameter

# class employee:
#     language = "py"
#     salary = 1200000

#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")

#     @staticmethod       #? Indicates that greet() does not require self
#     def greet():
#         print("Good Morning")
    

# Aditya = employee()  
# harry = employee()
# harry.language = "JS"     
# Aditya.getInfo()
# Aditya.greet()

#* ===========================================================================

#! Init method 
#? Dunder method which is automatically called

# class job:
#     language = "JS"
#     salary = 200000

#     def __init__(self):
#         print("I am creating an object")

# Rohan = job()  #? Whenever you make an object dunder method will be called
#! Only init will be called when object is formed     


class job:
    language = "JS"
    salary = 200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

Rohan = job("Rohan", 220000, "Python")

print(Rohan.name, Rohan.salary)

