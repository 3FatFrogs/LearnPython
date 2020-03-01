
# A set is an unordered collection of items. 
# Every element is unique (no duplicates) and must be immutable (which cannot be changed)
# However, the set itself is mutable. We can add or remove items from it.

print("\n=== Example of sets ================================================")

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)


# set of mixed datatypes with mutable items
#my_set = {1, 2, [3, 4]}

my_set = {1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, }  #set do not have duplicates
a = len(my_set)
print(a)
print(my_set)



print("\n=== An empty set ===================================================")
my_set1 = {}  # this is a dictionary
my_set2 = set() #  this is a set

print(my_set1, type(my_set1))
print(my_set2, type(my_set2))


print("\n=== Change a set ===================================================")
my_set = {1, 2, 3}
pippo = {4, 5, 6}

print("\n-- add an element -- ")
pippo.add(7)  # add one element
pippo.add(8) 
print(pippo)


print("\n-- add multiple elements -- ")
pippo.update({9,10})
print(pippo)


my_set.update(pippo)
print(my_set)


print("\n-- remove an element --")
my_set.remove(9)  # remove an element if exist, oterwise an error
print(my_set)

print("\n-- remove an element if exists --")
my_set.discard(90)  # remove an element if exist, oterwise an error
print(my_set)



print("\n-- randomly pop an element --")
print("initial = ", pippo)
print("remove  = ", pippo.pop())
print("final   = ", pippo)

print("\n-- remove all elements --")
pippo.clear()
print(pippo)


print("\n=== Operations =====================================================")

start = 0
size = 10
diff = 6
a = {x for x in range(start, size)}
b = {x for x in range(start + diff, size + diff)}
print("a = ", a)
print("b = ", b)

print()
print("union = ", a|b)
print("union = ", a.union(b))


print()
print("Intersection = ", a&b)
print("Intersection = ", a.intersection(b))


print()
print("Difference = ", a-b)
print("Difference = ", a.difference(b))


print()
print("Symmetric Difference = ", a^b)
print("Symmetric Difference = ", a.symmetric_difference(b))

