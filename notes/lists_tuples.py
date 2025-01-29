
#* LIST IS AN MUTABLE OBJECT

friends = ["Aditya", "rohan", "fil0st", "mooda"]

#! Append
friends.append("hello") #? Adds a "Term" in the end
print(friends)

#! Sort
l1 = [1,5,22,45,21, 23, 9]
l1.sort() #? sorts in order
print("Sorted string: ", l1)

#! Reverse
l1.reverse() #? reverses the order of lists
print("Reversed String: ", l1)

#! insert
friends.insert(2,"Nigga") #? inserts Nigga at index 2
print(friends)

#! pop
print(friends.pop(3)) #? Removes the term at that index and returns the new list


#! remove
friends.remove("hello") #? removes that term from the list
print(friends)

#* Tuple is an immutable object

b = () #! Empty tuple
c = (1,) #! Tuple with single element
a = (1 , 2 ,3 ,False, "Rohan", 2) #! Tuple with multiple elements


#! Count
no = a.count(2) #? counts the number of "TERM" appeared
print(no)

#! Index
ind = a.index(2) #? returns the index of "TERM"
print(ind)

#! In
print(2 in a) #? Is the "TERM" in the tuple?


