#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getAutocompleteScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY documentTitles
#  2. STRING_ARRAY documentBodies
#  3. STRING_ARRAY queries
#

def getAutocompleteScores(documentTitles, documentBodies, queries):
    # Write your code here
    '''
    have to find the highest score it can autocomplete to
    step 1: figure out what it can complete to
    step 2: figure out the scores of each
    step 3: return the highest score
    '''
    # our return array 
    scores = []

    # read all words into a dictionary with key = word, value = [n,m]
    # n = title ocurrences, m = body occurrences 
    words = createWordDictionary(documentTitles, documentBodies)

    # now that we have ocurrences, get scores for every word we've seen
    wordScores = assignScores(words)


    # calculate scores for every query
    for query in queries:
        possibleWords = findPossibleWords(query, wordScores)
        highestScore = 0 # if no possible words, will still add 0 to scores array
        for word in possibleWords:
            tempScore = wordScores[word]
            if tempScore > highestScore:
                highestScore = tempScore
        scores.append(highestScore)
    return scores

def findPossibleWords(start, words):
    # given the start of the word, find out
    # what it can complete to
    possibleWords = []

    # go thru every word and see if can complete 
    for word in words.keys():
        if canComplete(start, word):
            possibleWords.append(word)

    return possibleWords



def createWordDictionary(documentTitles, documentBodies):
    # given a word, get the total score across the input
    # returns zero if word not in the documents 
    words = {}
    for title in documentTitles:
        titleWords = title.split()
        for word in titleWords:
            if word not in words:
                words[word] = [1, 0]
            else:
                words[word][0] += 1

    for body in documentBodies:
        bodyWords = body.split()
        for word in bodyWords:
            if word not in words:
                words[word] = [0, 1]
            else:
                words[word][1] += 1
    
    return words

def assignScores(words):
    wordsScores = {}
    for key, value in words.items():
        score = int(value[0]*10 + value[1]*1)
        wordsScores[key] = score

    return wordsScores

def canComplete(target, word):
    if target > word:
        return False

    for i in range(len(target)):
        if target[i] != word[i]:
            return False
    
    # if we've made it this far, every char in target 
    # was in word so it can complete 
    return True
    



    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    documentTitles_count = int(input().strip())

    documentTitles = []

    for _ in range(documentTitles_count):
        documentTitles_item = input()
        documentTitles.append(documentTitles_item)

    documentBodies_count = int(input().strip())

    documentBodies = []

    for _ in range(documentBodies_count):
        documentBodies_item = input()
        documentBodies.append(documentBodies_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    result = getAutocompleteScores(documentTitles, documentBodies, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
