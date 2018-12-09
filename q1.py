# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



# MAIN SOLUTION -----------------------------------------------------------------
canjump=0

def solution(A):
    # write your code in Python 3.6
    # ways you can reach the end of the array 
    # can either do even or odd jumps 
    jumpcount=1
    for i in range(len(A)):
        jump(findSmallestOdd(i, A), A, jumpcount)
        return canjump
        
# RECURSIVE FUNCTION ------------------------------------------------------------------
def jump(pos, A, jumpcount):
    
    # base case 
    if pos == len(A)-1: # at end! hooray, increment canjump
        canjump+=1
    
    # keep jumping 
    if jumpcount%2==1:
        # odd jump, odd rules
        for i in range(pos, len(A)):
            if validOdd(pos, i, A):
                jump(i, A, jumpcount+1) # break into smaller problems
            else:
                break
    else:
        # even jump, even rules
        for i in range(pos, len(A)):
            if validEven(pos, i, A):
                jump(i, A, jumpcount+1)
            else:
                break
            
# HELPER FUNCTIONS ------------------------------------------------------------------------------

def validOdd(pos, i, A):
    # is jumping from pos to i valid in A, given odd jump?
    if i==findSmallestOdd(pos, A):
        return True
    else:
        return False
    
def validEven(pos, i, A):
    # is jumping from pos to i valid in A, given even jump?
    if i==findSmallestEven(pos, A):
        return True
    else:
        return False
    
def findSmallestOdd(pos, A):
    smallest=101
    smallpos=0
    for i in range(pos, len(A)):
        if A[i] > A[pos] and A[i]-A[pos] < smallest:
            smallest=A[i]
            smallpos=i
    return smallpos

def findSmallestEven(pos, A):
    smallestDiff=101
    smallpos=0
    for i in range(pos, len(A)):
        if A[i] < A[pos] and A[pos]-A[i] < smallestDiff:
            smallestDiff=A[i]
            smallpos=i
    return smallpos

        