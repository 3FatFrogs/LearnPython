
#A tuple in Python is similar to a list. The difference between the two 
#is that we cannot change the elements of a tuple once it is assigned whereas, 
#in a list, elements can be changed.

# https://www.programiz.com/python-programming/tuple

my_tuple = ()
my_list = []

print(my_tuple, type(my_tuple))
print(my_list, type(my_list))


print("\n=== Tuple having integers ===========================================================")
my_tuple = (1, 2, 3)
print(my_tuple)

print("\n=== tuple with mixed datatypes ======================================================")
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

print("\n=== nested tuple ===================================================================")
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

print("\n=== tuple unpacking is also possible ===============================================")
a,b,c = my_tuple
print(a, type(a))
print(b, type(b))
print(c, type(c))

print("\n=== Access Tuple Elements ==========================================================")
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#n_list = ["mouse", [8, 4, 6], (1, 2, 3)]
print(n_tuple[0]) 
print(n_tuple[0][3]) 
print(n_tuple[1]) 
print(n_tuple[-1]) 
print(n_tuple[-2]) 

print("\n=== Slicing ========================================================================")
#We can access a range of items in a tuple by using the slicing operator - colon ":".
n_tuple = (1,2,3,4,5,6,7,8,9)
print(n_tuple) 
print("n_tuple[0:4]   = ", n_tuple[0:4]) 
print("n_tuple[:4]    = ", n_tuple[:4]) 
print("n_tuple[7:]    = ", n_tuple[7:]) 
print("n_tuple[2:4]   = ", n_tuple[2:4]) 
print("n_tuple[-1:-4] = ", n_tuple[-1:-4]) 
print("n_tuple[-4:-1] = ", n_tuple[-4:-1]) 


