

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, E):
    # write your code in Python 3.6
    if len(S)==1:
        return 1 # only need one chair for one guest
    
    # get guests for every time, and then find max in that array 
    numatparty=[]
    for i in range(max(E)):
        numatparty.append(0) 
    
    for i in range(len(S)):
        # add timerange to the array of num at party at each time
        for j in range(S[i], E[i]): # can only add from start to end time
            numatparty[j]+=1
    
    return max(numatparty)
        