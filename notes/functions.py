
#* Group of statements performing task!
#* Makes Reusing easy

# def greet():                #? Defining a function
#     print("Hello")

# greet()                     #? Executing an already defined function
# greet()                     #! Function call - Term

# def greet():
#     a = input("What is your name? ")
#     print(f"Hello {a}")

# greet()

#* Types of functions

#! Built in function
#? Already present in function example: len(), range(), print() etc
#! User defined function
#? Defined by us example: greet()

#* Functions with argument:

# def hello(name, ending):                          #? Name,ending = parameter, giving arguments !!
#     print(f"Hello Mr/Ms, {name}")
#     print(ending)
#     return 0                                      #? it makes the function take the value incase any variable ask

# a = hello("Aditya", "Thank you")
# print(a)


#* Default parameter value

# def hello(name, ending="Thank You"):              #? "Thank you" is a default value if no argument is passed for ending
#     print(f"Hello Mr/Ms, {name}")
#     print(ending)

# hello("Aditya")

#* Recursion
#! Calls itself

# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter a number: "))
# print(f"The factorial of {n} is {factorial(n)}")

