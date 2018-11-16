import sys
def isOdd(curr):
    # takes an integer and checks if it has odd digits
    # create a dict
    for i in str(curr):
        if int(i)%2 != 0:
            return True
    return False

for line in sys.stdin:
    # do for each line of input
    ops=0
    curr = int(line)
    
    # only reverse while it doesnt have odds
    while(isOdd(curr) == True):
        curr=curr+int(str(curr)[::-1])
        ops+=1
    print(ops, curr)