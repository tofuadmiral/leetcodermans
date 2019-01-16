class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
         # first, split into words
        words=s.split()
        words.reverse()
        wordstr=""
        for i in words:
            wordstr+=i + " "
        return wordstr[:len(wordstr)-1]
        