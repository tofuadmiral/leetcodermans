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
    1. using ocurrences, calculate score of each word
    2. find possible words for each query
    3. find highest score amongst possible words for each query
    4. return those scores
    '''
    # our return array 
    scores = []

    # read all words into a dictionary with key = word, value = score
    wordScores = createWordDictionary(documentTitles, documentBodies)

    # calculate scores for every query
    for query in queries:
        possibleWords = findPossibleWords(query, wordScores)
        highestScore = 0 # if no possible words, will still add 0 to scores array
        for word in possibleWords:
            if wordScores[word] > highestScore:
                highestScore = wordScores[word]
        scores.append(highestScore)
    
    return scores

def findPossibleWords(start, words):
    # return words start can autocomplete to
    possibleWords = []

    for word in words.keys():
        if canComplete(start, word):
            possibleWords.append(word)

    return possibleWords


def createWordDictionary(documentTitles, documentBodies):
    # create a dictionary with key = word, value = score
    words = {}
    for title in documentTitles:
        titleWords = title.split()
        for word in titleWords:
            if word not in words:
                words[word] = 10
            else:
                words[word] += 10

    for body in documentBodies:
        bodyWords = body.split()
        for word in bodyWords:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    
    return words

def canComplete(target, word):
    if target > word:
        return False

    if target == word[0:len(target)]:
        return True

    return False
    

if __name__ == '__main__':