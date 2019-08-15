class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        longest substring with no repeating characters
        
        abcabcbb
        
        therefor longest is abc, bc once abca then repeats
        
        naive approach:
            find every possible substring and see which ones 
            don't repeat, then keep track of that longest one
            
            time: O(n^2) 
            space: O(n) beacuse store every character in the string
            
        improvements? 
            two pointer method: 
                start at end and move pointer if we see a repeat, if not move 
                right pointer
                
                not sure if this will work so let's try naive method first
        """
 
        for i in range(len(s)):
            for j in range(i, len(s)):
                