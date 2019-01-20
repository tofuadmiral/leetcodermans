class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        diglist1=[]
        diglist2=[]
        s1list=version1.split(".")
        s2list=version2.split(".")
        
        # read splits into array 
        for i in s1list:
            if len(i)>0 and i[0]==0:
                start=self.removeLeading(int(i))
                diglist1.append(int(i[start]))
            else: # we don't need to remove leading zeros
                diglist1.append(int(i))

        for i in s2list:
            if len(i)>0 and i[0]==0:
                start=self.removeLeading(i)
                diglist2.append(int(i[start]))
            else: # we don't need to remove leading zeros
                diglist2.append(int(i))
        
        greater=1
        
        print(diglist1)
        print(diglist2)

        
        incre=0
        if diglist1[0]==diglist2[0]:
            for incre, (val1, val2) in enumerate(zip(diglist1, diglist2)):
                if val1 !=val2:
                    break
        # now we're there where theres a diff
        if diglist1[incre]==diglist2[incre]:
            greater=0
        elif diglist1[incre]>diglist2[incre]:
            greater=1
        elif diglist1[incre]<diglist2[incre]:
            greater=-1
        return greater
        
        
        
    def removeLeading(self, string):
        incre=0
        for i, val in enumerate(string):
            incre+=1
            if val!="0":
                break
        return incre
               
            