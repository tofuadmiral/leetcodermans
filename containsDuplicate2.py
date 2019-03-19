class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # contains duplicate 2
        
        '''
        
        want to see if two distinct i and j
        numsi and numsj are the same, and <= than k
        
        
        '''
        seen={}
        
        for i in xrange(len(nums)):
            if nums[i] in seen:
                # check if we also less than diff
                if abs(i-seen[nums[i]])<=k:
                    return True
                else:
                    seen[nums[i]]=i #reassign bc we got to new position
            else:
                seen[nums[i]]=i
                
        return False
        
        