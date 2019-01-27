class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        look for duplicates, 
        at least one duplicate, find it
        constant extra space
        can't modify the array
        runtime should be less than n squared
        one duplicate number, but could be more than one
        
        we know the sum of the numbers should be 
        """
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]==nums[j]:
                    return nums[i]
            
                