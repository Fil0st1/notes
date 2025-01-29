# def greatest(a,b,c):
#     return max(a,b,c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print(f"The greatest of {a}, {b}, {c} is {greatest(a,b,c)}")

# def ctof(c):
#     return (c * (9/5)) + 32

# c = int(input("Give the temperature in celcius: "))
# print(f"The temperature in farenheight is {ctof(c)}")


# def sumofn(n):
#     i = 0
#     total = 0  # Use a different name to avoid conflict with the built-in `sum` function
#     if n <= 0:
#         print("Enter a valid positive integer")
#     else:
#         while i <= n:  # Fix the loop condition
#             total += i  # Add i to the total
#             i += 1      # Increment i
#     return total

# n = int(input("Enter a positive integer n: "))
# print(f"The sum of the first {n} numbers is {sumofn(n)}")

# def ItoC(n):
#     a = n*2.54
#     return round(a, 2)

# n = int(input("Enter a number in inches: "))
# print(f"{n} inches in cm is {ItoC(n)}")

# def table(n):
#     for i in range(0, 11):
#         print(f"{n} X {i} = {n*i}")

# n = int(input("Enter a number: "))
# table(n)

# def star(n):
#     for i in range(n, 0, -1):
#         print("*" * i)

# n = int(input("Enter a number: "))
# star(n)