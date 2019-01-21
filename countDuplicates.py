#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countDuplicates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#


def countDuplicates(numbers):
    # Write your code here
    seen={}
    count=0
    for i in numbers:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    for key, value in seen.items():
        if value>1:
            count+=1
    return count
        

if __name__ == '__main__':