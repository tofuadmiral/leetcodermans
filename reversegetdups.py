import sys

def hasDups(curr):
    # takes an integer and checks if it has duplicate digits
    # create a dict of digits, loop thru and add, check before adding
    digdict={}
    for i in str(curr):
        if i in digdict: # that means we've already seen this key! 
            return True
        else:
            # we haven't seen this key, so insert it
            digdict[i]=int(i)
    return False

for line in sys.stdin:
    # do for each line of input
    ops=0
    curr=int(line)
    
    # only reverse while it doesnt have odds, but do for first one too
    curr=curr+int(str(curr)[::-1])
    ops=1
    while(hasDups(curr) == True):
        curr=curr+int(str(curr)[::-1])
        ops+=1
    print(ops, curr)