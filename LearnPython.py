
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

    
    




for x in range(-5,15):
   print(x%4) 


def solution(A, K):
    #number of movements

    n = len(A)
    
    if(n<1)
        return A
    
    for i in range(0,K%len(A)):
        t = A[n-1]
        for x in range(n-1,-1,-1):
            A[x] = A[x-1]
        A[0] = t

print(solution(([3, 8, 9, 7, 6], 3)))