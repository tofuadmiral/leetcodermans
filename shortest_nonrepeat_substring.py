class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        no repeats, longest substring
        
        go through, make every possible substring without repeats,
        
        store seen chars in the set, overwrite the set when we know 
        we have reached the seen chars 
        
        
        """
        
        # create an emtpy set of characters
        chars = set()
        longest = 0
        sofar = 0
        
        # iterate through string
        for i in range(len(s)):
            # reset vars
            chars = set()
            chars.add(s[i])
            sofar = 1
            
            # check next item and update
            for j in range (i+1, len(s)):
                if s[j] not in chars:
                    chars.add(s[j])
                    sofar+=1
                else:
                    if sofar > longest:
                        longest = sofar
        return longest
                    
                