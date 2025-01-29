
#* Unordered
#* Mutable
#* Indexed
#* Cannot contain duplicate keys

marks = {
    "Aditya": 100,
    "Tiwari": 65,
    "Rohan": 99,
    0: "Aditya",
}

#! Methods

# print(marks.items())  #? Gives items in tuple forms

# print(marks.keys())  #? Gives items present in LHS
# print(marks.values())  #? Gives items present in RHS

marks.update({"Aditya": 99, "Singhlord": 80}) #? Edits/adds a key cuz DICT IS "MUTABLE"
print(marks)


#!Difference between these both lines is that:
#?if the key is not present in the dictionary the square brackets give errors while the curve bracket gives NONE

print(marks.get("Aditya2")) #? Prints None
print(marks["Aditya2"]) #? Prints error
 



