
print("\n=== Nested list ================================================================")
my_list = ['h','e','l','l','o']
my_tuple = ('h','e','l','l','o')

print(my_list)
print(my_tuple)

print(my_list[2])
print(my_tuple[2])

print("\n=== Nested list ================================================================")
my_list = ["Happy", [2,0,1,5]]
print(my_list)


print("\n=== Add/Remove element to a list ===============================================")
n_list = []
for x in range(10): n_list.append(x)
print(n_list)

x_list = [3,3,3]
n_list.extend(x_list)
print(n_list)

del n_list[1:4]
print(n_list)

a = n_list.pop(1)  #removes and returns the last item if index is not provided.
print("Pop value = ",a)
print(n_list)

n_list.clear()  #empty list
print(n_list)


print("\n=== Combine two or more list ===================================================")
a_list = [1,2,3]
b_list = [6,7,8]
c_list = a_list + b_list

print(a_list)
print(b_list)
print(c_list)

print("\n=== Create list ================================================================")
a_list = [x**2 for x in range(10)]
print(id(a_list), a_list)

a_list = [x**1 for x in range(10)]
print(id(a_list), a_list)
