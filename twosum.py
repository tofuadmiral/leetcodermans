class Solution(object):
    # return two integers, make sure we return the indexes of the integers that add up to the target sum
    def twoSum(self, nums, target):
        for i in range(len(nums)): # loop through once
            for j in range (len(nums)): # loop through again while first pointer on the first integer
                if (nums[i] + nums[j]) == target: # conditional to see whether it is the answer or not 
                    return [i, j]
                else:
                    continue
                
            