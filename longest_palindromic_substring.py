class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        longest palindromic substring
        
        s, find substring that is also palindromic 
        
        find a palindrome
            start at ends, compare and loop while not equal
            if we reach where they're equal, then we have a palindrome
            
        to find the longest palindrome
            find all palindromes and then store the longest one so far
        
        or
            start at ends, that should be the longest possible, 
            then work your way down 
        
        """
        
        # brute force, make every possible palindrome 
        
        
        if len(s) == 1:
            return s
        elif not s:
            return ""
        
        longest = s[0]

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if (j-i)+1 > len(longest):
                    if s[i:j+1] == ''.join(reversed(s[i:j+1])):
                        longest = s[i:j+1]
                else:
                    continue
        return longest
                    
                    
        