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
        
        # create an emtpy map of characters
        char_map = {}
        start = 0
        longest = 0

        for index, char in enumerate(s):

            # iterate thru
            # if we're at a char that we've seen and it's past where we used to be
            # then start looking again from there + 1 bc that can't be longest, 
            # unless it is longest, in which case check and update it

            if char in char_map and char_map[char] >= start:
                length = index - start
                longest = max(length, longest)
                start = char_map[char] + 1
            char_map[char] = index
        
        # we might reach end before finishing this, so check if the last string is the longest
        length = len(s) - start
        return max(longest, length)

 