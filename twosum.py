class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # begin coding

        # start by brute force, two for loops
        '''
        numInts = len(nums)
        for i in range(numInts):
            for j in range(i+1, numInts):
                if nums[j] == target - nums[i]:
                    return [i, j]
                else:
                    continue
        '''

        # now try using a hash table
        numDict = {}

        # first put everything into the hash table, in this case a python dictionary
        for i in range(len(nums):
            numDict[i] = nums[i]
        
        # loop thru and check if complement exists in dict, if yes, then equals sum, if no then idk

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDict and complement != nums[i]:
                return [i, dict.get(complement)]



