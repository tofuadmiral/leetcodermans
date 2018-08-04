class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # begin coding

        # start by brute force, two for loops
        numInts = len(nums)
        for i in range(numInts):
            for j in range(i+1, numInts):
                if nums[j] == target - nums[i]:
                    return [i, j]
                else:
                    continue