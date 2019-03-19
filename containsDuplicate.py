class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # see if we have any repeats
        seen={}
        for i in xrange(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]]=1
        return False
        