
#! While loop

# l = [2 , 44, 4545, 4525]
# i = 0

# while (i<len(l)):
#     print(l[i])
#     i += 1

#! For Loop
# for i in range(0, 100, 10):  #? range(start, stop, step_size) Step-size is usually not used with range()
#     print(i)


#! A for loop is used to iterate through a sequence like list, tuple, or string (iterables)
#! For loop iterate


#* List/Tuple
l = ["hello", "How r u", 99, False]

# for i in l:
#     print(i)

# #* String
# s = "Aditya"

# for i in s:
#     print(i)

#! For loop with else (Interview)

# for i in l:
#     print(i)
# else:
#     print("Done") #? This is printed when the loop exhausts


#! Break and Continue Statement

# for i in range(0, 100):
#     if ( i == 35):
#         break #? Exit the loop right now
#     print(i)

# for i in range(0, 100):
#     if ( i == 35):
#         continue #? Skip this iteration
#     print(i)

#! Pass statement
#* IT is a null statement which instructs to do nothing

for i in range(0, 100):
    pass

i = 0
while(i<45):
    print(i)
    i += 1