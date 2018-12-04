#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # first, read in the magazine words into a dictionary
    # this would be linear time, key = word, value = 1
    words={}
    for i in magazine:
        if i not in words:
            words[i]=1
        elif i in words:
            words[i]+=1  # if already exists, increment by 1

    # now, check if we have all the words we need
    flag=True
    for i in note:
        if i in words and words[i]!=0:
            words[i]-=1
        else:
            flag=False
    
    if flag:
        print('Yes')
    else:
        print('No')




if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
