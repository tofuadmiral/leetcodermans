class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        find the element that doesnt appear twice in the array,only apprears once
        
        
        thus add all items and number of times we see to dictionary
        then loop through values, if val = 1, print the key
        """
        numDict={}
        for i in nums:
            if i not in numDict:
                numDict[i]=1
            if i in numDict:
                numDict[i]+=1
        for i in numDict.keys():
            if numDict[i]==1:
                return i

            
        