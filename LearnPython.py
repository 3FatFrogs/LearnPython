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
def passing_cars(A):
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



#=== Find the minimal average of any slice containing at least two elements. ==
def MinAvgTwoSlice(A):
    minimal_average = float('inf')
    starting_position = 0
    for i in range(0, len(A)+1):
        for j in range(i+2, len(A)+1):
            temp = sum(A[i:j])/(j-i)
            if temp < minimal_average:
                starting_position = i
                minimal_average = temp
            print(i,j, A[i:j], sum(A[i:j])/(j-i))
        
    return starting_position


# =============================================================================
# def ciccio(A):
#     min_index = 0
#     print(A)
#     # why prefix some? - just to calculate the some between two places without using two loops
#     prefix_sum = [0] * len(A)
#     prefix_sum[0] = A[0]
#     for i in range(1, len(A)):
#         prefix_sum[i] = prefix_sum[i - 1] + A[i]
#     print("prefix_sum = ", prefix_sum)
#     
#     min_avg = float('inf')
#     # start from slice p ie. from start, this is start and act as P in problem statement and Q would be the q_end_index as shown below
#     slice_p_from_index = 0
#     
#     for q_end_index in range(1, len(A)):
#         print("===============")
#         #print("From P:slice_p_from_index= " + str(slice_p_from_index) + "  To Q: i= " + str(q_end_index) + " slice " + str(A[slice_p_from_index:q_end_index + 1]))
#         #print("Slice length " + str(q_end_index - slice_p_from_index + 1))
#         # get the some for position P,Q - ie. from slice_p_from_index to i positions and davide by the slice length
#         average = (prefix_sum[q_end_index] - prefix_sum[slice_p_from_index] + A[slice_p_from_index]) / (q_end_index - slice_p_from_index + 1)
#         print("average = ", average)
#         # check for minimum average so far
#         if average < min_avg:
#             min_avg = average
#             # hold the index for minimum average value
#             min_index = slice_p_from_index
#     
#         print("min_avg " + str(min_avg))
#         # this is to find out the next starting position for slice_p_from_index
#         # idea is to skip all the items found so far up to q_end_index-1, to skip and start from q_end_index we have to proof that the next slice min average
#         # can be less than the current minimum average
#         # that can only happen if and only if current Item A[q_end_index] is less than the minimum average
#         # if so we start taking array slice from current Item A[q_end_index] and make slice with next Item
#         print("Index = " + str(q_end_index) + " Item " + str(A[q_end_index]))
#         if A[q_end_index] < min_avg:
#             print("min index found....Item < min_avg, slice_p_from_index changed to Index")
#             slice_p_from_index = q_end_index
#         print("")
#     return min_index
# 
# x = [4,2,2,5,1,5,8]
# for i, j in enumerate(x):
#     print(i,j)
# print("======================")
# print(x[0:1])
# print(x[0:2])
# print(x[0:3])
# print(x[3:])
# 
# 
# #x = [-3, -5, -8, -4, -10]
# 
# 
# 
# print("======================")
# pippo = MinAvgTwoSlice(x)
# print(pippo)
# 
# print("======================")
# pippo = ciccio(x)
# print(pippo)
# 
# 
# =============================================================================


#=== GenomicRangeQuery ========================================================
def solution(S, P, Q):
    # write your code in Python 3.6
    s_list = list(S)

    for i,j in enumerate(s_list):
        if    j == 'A':   s_list[i] = 1
        elif  j == 'C':   s_list[i] = 2
        elif  j == 'G':   s_list[i] = 3
        elif  j == 'T':   s_list[i] = 4
    
    result = []
    for i in range(0, len(P)):
        result.append(min(s_list[P[i]:Q[i]+1]))
    
    return result


def GenomicRangeQuery(S,P,Q):
    # write your code in Python 3.6
    s_list = list(S)    
    result = [0] * len(P)
    for i in range(0, len(P)):        
        pippo = s_list[P[i]:Q[i]+1]
        
        if 'A' in pippo:     result[i] = 1
        elif 'C' in pippo:   result[i] = 2
        elif 'G' in pippo:   result[i] = 3
        else:                result[i] = 4
                
    return result
    
        
def solution2(S, P, Q):
    cost_dict = {'A':1, 'C':2, 'G':3, 'T':4}

    curr_counts = [0,0,0,0]
    counts = [curr_counts[:]]
    for s in S:
        print(s,counts)
        curr_counts[cost_dict[s]-1] += 1
        counts.append(curr_counts[:])

    print(curr_counts)
    print(counts)
    
    
    
    print("========")
    print(cost_dict)
    
    results = []
    for i in range(len(Q)):
        counts_q = counts[Q[i] + 1]
        counts_p = counts[P[i]]
        
        print("====================")
        print("counts_q = ", counts_q)
        print("counts_p = ", counts_p)
        print(Q[i], P[i], S[Q[i]])



        if Q[i] == P[i]:
            results.append(cost_dict[S[Q[i]]])
            print("--->>" , cost_dict[S[Q[i]]])
            
        elif counts_q[0] > counts_p[0]:
            results.append(1)
        elif counts_q[1] > counts_p[1]:
            results.append(2)
        elif counts_q[2] > counts_p[2]:
            results.append(3)
        elif counts_q[3] > counts_p[3]:
            results.append(4)

    return results   
    
    


solution2('CAGCCTA', [2, 5, 0], [4, 5, 6])



x = ['C', 'A', 'G', 'C', 'C', 'T', 'A']




#=== Distinct ========================================================
#Compute number of distinct values in an array.
def Distinct(A):
    return list(set(A))
    

#=== Determine whether a triangle can be built from a given set of edges. =====
def Triangle(A):
      A.sort()
      for i in range(0,len(A)-2):
          if(A[i] + A[i+1]) > A[i+2]:
              return 1
      
      return 0








# =============================================================================
# MaxProductOfThree
# Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
# =============================================================================
def solution(A):
    max_value = -float('inf')

    A.sort()
    for i in range(len(A)-2):
        max_value = max(A[i] * A[i+1] * A[len(A)-1], max_value)

    
    return max_value
 




#=== Compute the number of intersections in a sequence of discs. ==============







































    
