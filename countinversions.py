#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
numinv=0

def countInversions(arr):
    # count the number of inversions in the array arr
    n=len(arr)
    numinv=0
    for i in range(n):
        for j in range(i, n):
            if arr[i]>arr[j]:
                # this means it's an inversion
                numinv+=1
    return numinv

    ## now do it via mergesort
    # we want to do this recusrively 
    temparray=[None] for i in range(n)

def mergesort(self, arr, temparray, leftstart, rightend):
    if leftstart>=rightend:
        return 
    mid=leftstart+rightend/2
    mergesort(arr, temparray, leftstart, mid)
    mergesort(arr, temparray,  mid+1, rightend)
    mergehalves(arr, temparray, leftstart, rightend)

def mergehalves(arr, temparray, leftstart, rightend):
    # can't do it in place, so let's make a temporary array 
    # to make this more efficient, gives us a new temp that we always pass in
    mid=(leftstart+rightend)/2
    left=leftstart
    right=mid+1
    index=leftstart
    while(left<=mid and right<=rightend): # go through the two halves of the array
        # copy all the lefts if less, then right if not less
        if arr[left]<=arr[right]:
            temparray[index]=arr[left]:
            left+=1
        else:
            # copy the right element if it's bigger
            # this also means that it's an inversion
            temparray[index]=arr[right]
            numinv+=1
            right+=1
        index+=1 # continue on in the temparray
    
    # now our temparray has all the elements from the right and left half 
    # might end it early and not copy all the right or left elements, so let's make sure we do
    if left>mid: # copy all the remaining right elements
      for i in range(right, rightend):
          temparray[index]=arr[i]
          index+=1
    if right>rightend: # copy all the remaining left elements, which means they're all inversions too
        for i in range(left, mid):
            temparray[index]=arr[i]
            index+=1
            numinv+=1
    
    # now copy everything back into the original array
    for i in range(leftstart, len(temparray)):
        arr[i]=temparray[i]






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
