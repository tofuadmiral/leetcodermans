class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # peak means greater than neighbors
        # find any peak and return its index
        
        for i in xrange(len(nums)):
            # should be in logarithmic complexity 
            if len(nums)==1:
                return 0
            if i==0:
                if nums[i]>nums[i+1]:
                    return i
                else:
                    pass
            if len(nums)==2:
                if nums[0]<nums[1]:
                    return 1
                else:
                    return 0
            if i==len(nums)-1: # we're at the last one
                if nums[i] > nums[i-1]:
                    return i
            if nums[i] > nums[i+1] and nums[i]>nums[i-1]:
                return i
            
            
        