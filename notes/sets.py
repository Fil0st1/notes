
#* Unordered
#* Unindexed
#* Cannot change items in sets
#* Cannot contain duplicate values

e = set() #! Empty set, dont use s={} as this will create an empty dictionary

#! Sets do not repeate elements
#! It will ignore repeated elements


#! Methods

s1 = { 1, 2, 2, 55, 67, 32}
s2 = { 1,55, 34, 78}

#! Add
# s1.add(330) #? Adds a "TERM" in the sets

# print(len(s1)) #? sends length of the set

# s1.remove(2) #? Removes a element from set

# s.pop() #? Removes a random element (DONOTUSE)
#s.clear() #? Clears ur set


#! Maths Methods

print(s1.union(s2)) #? Takes the s1 set and s2 set
print(s1.intersection(s2)) #? Takes the common values b/w two

