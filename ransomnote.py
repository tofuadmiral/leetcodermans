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
        # add to the words if it's not there, but if it is, add that we have two words
        if i not in magazine:
            words[i]=1
        if i in magazine:
            words[i] += words[i]
    
    flag=True
    # now, go through the note array and make sure we have all the words 
    for i in note:
        if i not in words:
            flag = False
    

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
