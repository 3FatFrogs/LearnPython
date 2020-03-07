for x in range(100):
    print()

print("Hello")




#=== BinaryGap ======================== 
def fun(N):
    if N<2:
        return 0

    result = 0
    count = 0

    for x in "{0:b}".format(N):
        if x == '0':
            count = count +1
        else:
            if count > result:
                result = count
            count = 0
            
    return result 

    
    




#=== Remove duplicate from a list ======================== 
def remove_duplicate(my_list):    
    for x in my_list:
        if my_list.count(x) > 1:
            my_list.remove(x)


def remove_non_duplicate(my_list):
    for x in range(len(my_list)):
        if my_list.count(x) == 1:
            my_list.remove(x)



a = [1,2,3,4,5,6,3,0]
a.sort()
b = a.copy()



print("=======")
print(id(a), a)
print(id(b), b)

remove_duplicate(a)
remove_non_duplicate(b)

print(id(a), a)
print(id(b), b)


