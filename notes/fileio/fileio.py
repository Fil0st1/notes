
#* Read the file

# f = open("data.txt", "r")       #? r ==> read mode
# data = f.read()

# print(data)
# f.close()

#* Write

# st = "Hello to you too "
# f = open("data.txt", "w")       #? w ==> write mode
# f.write(st)

#* Modes of opening a file

#? r – open for reading
#? w - open for writing
#? a - open for appending
#? + - open for updating.
#? ‘rb’ will open for read in binary mode.
#? ‘rt’ will open for read in text mode. 


#* Readline / readlines function

f = open("data.txt")
# lines = f.readlines()  #? Reads all line

lines = f.readline()    #? Reads line by line
print(lines, type(lines))

f.close()


#! With Statement:

f = open("data.txt")
print(f.read())
f.close()

                        #* This same statment can be written by with function

with open("data.txt") as f:
    print(f.read())     #? Will automatically close the file