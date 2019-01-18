class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        print(version1)
        print(version2)
        diglist=[]
        # chop off the leading eros
        s1=self.removeLeading(version1)
        s2=self.removeLeading(version2)
        
        
        
    def removeLeading(string):
        i=0
        while string[i]=="0" and string[i+1]!= ".":
            i+=1
        return i
               
            