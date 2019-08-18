class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        
        median of two sorted arrays
        
        merge both into an array 
        count how many additions we're doing to the merged array 
        
        once we reach the halfway point then return that 
        
        check if even or odd, then calc median
        
        if even 
            merge two lists until 
        
        """
        
        
        if (len(nums1)+len(nums2))% 2:
            status = "even"
        else:
            status = "odd"
            
        counter = 0
        median = 0
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if counter == (len(nums2)+len(nums1))/2 - 1:
                median = min(nums1[i], nums2[j])
            if nums1[i] < nums2[j]:
                i+=1
                counter+=1
            else:
                j+=1 
                counter+=1
                
        if status == "odd":
            median = median + min(nums1[i+1], nums2[j+1])
            return median
        else:
            return median 
            
                
                
        