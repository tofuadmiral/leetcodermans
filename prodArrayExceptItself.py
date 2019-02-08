class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # product of array except itself
        # run through first and make array of elements
        # where it's the sum so far, not include that element
        sumsofar=[0]*len(nums)
        sumafter=1
        for i in range(len(nums)):
            if i==0:
                sumsofar[i]=1
            if i==1:
                sumsofar[i]=nums[0]*1
            else:
                sumsofar[i]=nums[i-1]*sumsofar[i-2]
        
        # now we have sum so far, so go backwards and get sum after and then
        # multiply back into our array
        for i in range(len(nums)-1, 0, -1):
            sumafter*=nums[i+1]
            sumsofar[i]*=sumafter
            
        return sumsofar
            
        