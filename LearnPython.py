import math

for x in range(100):
    print()

print("Hello")




#=== BinaryGap ================================================================
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

                                                          

#=== Remove duplicate from a list ============================================= 
def remove_duplicate(my_list):    
    for x in my_list:
        if my_list.count(x) > 1:
            my_list.remove(x)


#=== Remove non duplicate from a list ========================================= 
def remove_non_duplicate(my_list):
    for x in range(len(my_list)):
        if my_list.count(x) == 1:
            my_list.remove(x)



#== CyclicRotation ============================================================
def CyclicRotation(A, K):
        
    if len(A) < 2:
        return A
    
    #check if all elements are the same
    if len(A) == A.count(A[0]):
        return A
    
    
    for i in range(K%len(A)):
        last = A[len(A)-1]
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j-1]
        A[0] = last
    return A
        


#=== OddOccurrencesInArray ====================================================
def OddOccurrencesInArray(A):
    r = 0
    for x in A:
        r ^= x
    return r



#=== FrogJmp ==================================================================






#=== PermMissingElem ==========================================================
def PermMissingElem(A):
    partial_sum = 0
    for x in A:
        partial_sum += x
    n = len(A)+1
    return (int)(0.5*n*(n+1))-partial_sum    



