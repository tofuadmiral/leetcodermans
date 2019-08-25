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
        
        
        # not brute force, linear time solution

        longest = 0
        for i in range(len(s)):
            temp = find_palindromes(self, s, i, i)
            if len(temp) > len(longest):
                longest = temp
        
        return longest
    
    def find_palindromes(self, s, l, r):

        # if we're making a palindrome rn, continue to make them
        # once we're not, exit and return the palindrome
        temp = ""
        while (l>0 and r<len(s) and s[l] == s[r]):
            l-=1
            r+=1
        temp = s[l:r+1]
        return temp
                    
        