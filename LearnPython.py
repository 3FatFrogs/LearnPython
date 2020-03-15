import math

for x in range(100):
    print()




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



#=== Remove negative from list ================================================
def remove_negative1(A):
    B = A.copy()
    for x in B:
        if x<0:
            A.remove(x)

def remove_negative2(A):
    B = A.copy()
    for x in B:
        if x<0:
            A.remove(x)

   
    
my_list = range(-10,11)
my_list = list(filter(lambda x: x >= 0, my_list))

#=== Find minimila difference==================================================
def MinimialDiff(A):
    
    if len(A) == 2:
        return abs(A[0]-A[1])
    
    tot_sum = sum(A)
    min_value = float('inf')
    left_sum = 0
    for x in range(0,len(A)-1):
        if A[x] == 0:
            continue
        left_sum += A[x]
        temp = abs(2*left_sum-tot_sum)
        min_value = min(min_value,temp)
        
    return min_value


#=== Find missing integer =====================================================
def MissingInteger(A):    
    
    #remove all negeative    
    A = list(filter(lambda x : x>0, A ))
    
    if len(A) < 1:
        return 1    
    
    #remove duplicates
    A = list(dict.fromkeys(A))
    
    A.sort()
    
    for k in range(len(A)):
        if A[k] != k+1:
            return (k+1)
    
    return A[len(A)-1]+1




#=== Small frog cross the river ================================================
def FrogRiverOne(X,A):
        
    if len(A) < X:
        return -1
    
    leaves = set()
    
    count = -1
    
    for x in A:
        leaves.add(x)
        count += 1
        if len(leaves) == X:
            return count
    
    return -1


#=== Check whether array A is a permutation ===================================
def PermCheck(A):
    if max(A) == len(A):
        #remove duplicate
        A = list(dict.fromkeys(A))
        if max(A) == len(A):
            return 1
    return 0



'''
Calculate the values of counters after applying all alternating operations : 
increase counter by 1; set value of all counters to current maximum.
'''
def MaxCounter(N,A):
    
    temp = [0] * N #list of zeros
    temp_max = 0
    max_value = 0

    N1 = N + 1
    for x in A:
        if x == N1:            
            max_value = max(max_value,temp_max)
        else:
            temp[x-1] = max(temp[x-1], max_value) + 1
            temp_max = max(temp_max,temp[x-1])
    
    for x in range(N):
        temp[x] = max(max_value, temp[x])
        
    return temp



#=== Compute number of integers divisible by k in range [a..b]. ===============
def compute_number_of_integer(A,B,K): 

    return 1 + math.floor(B/K)- math.ceil(A/K)
    


   
        
#=== PassingCars ==============================================================
def passing_cars()
    result = 0
    count_zeros = 0
    for i in A:
        if i == 0:
            count_zeros += 1
        else:
            result += count_zeros
    
    
    if result > 1000000000:
        result = -1
    
    return result







