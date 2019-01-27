#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
