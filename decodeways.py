class Solution(object):
    
    def recDecoding(self, s, index):
        if index==len(s)-1:
            return 1

        if index<=len(s)-2:
            if int(s[index]+s[index+1])<27:
                return int(2 + self.recDecoding(s, index+1) + self.recDecoding(s,index+2))
            else:
                return int(1+self.recDecoding(s, index+1))
        if s[index]=="":
            return 0


            
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        return self.recDecoding(s, 0)
    

        