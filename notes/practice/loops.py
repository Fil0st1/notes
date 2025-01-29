a = int(input("Enter a number you want a multiplication table of: "))
b = a*10 + a
for i in range(0,b, a):
    print(i)

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if "S" in i:
        print(f"Hello mr. {i}")

a = int(input("Enter a number you want a multiplication table of: "))
b = a*10 + a
i = 0
while (i<b):
    print(i)
    i += a

a = int(input("Enter a number you want to check for prime number: "))


if a<= 1:
    print("The given number is not a prime number!")
else:
    is_prime = True
    for i in range(2,a):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
            print("The given number is a prime number!")
    else:
            print("The given number is not a prime number!")

a = int(input("Enter the n number of terms you want to add: "))
b = a + 1

if (a<=0):
    print("Please enter a positive integer!")
else: 
    sum = 0
    i = 0
    while (i<=a):
        sum += i
        i += 1
    print(f"The sum of first {a} terms is {sum}")

a = int(input("Enter a number you want the factorial of: "))

if a < 0:
    print("Please enter a positive integer!")
elif a == 0:
    print("The factorial of 0 is 0!")
else:
    factorial = 1
    for i in range(1, a+1):
        factorial *= i
    print((f"The factorial of {a} is {factorial}"))


a = int(input("Enter a number you want the reversed multiplication of: "))

for i in range(10,0,-1):
    print(f"{a} X {i} = { a * i }") 

a = int(input("Enter a number: "))

for i in range(1,a+1):
    if (i==1 or i==a ):
        print("*" * a, end="")
    else:
        print("*", end="")
        print(" " * (a-2), end="")
        print("*", end="")
    print("")