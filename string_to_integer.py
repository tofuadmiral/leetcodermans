class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ''' 
        first discard whitespace
        
        then check if first non-white is valid character
        then check for negative
        then continue and contactenate to the string, to then convert to int
        
        '''
        int_str = ""
        
        if not str:
            return 0
        
        i = 0
        while str[i] == ' ':
            i+=1
            
        # now we're at where there's no whitespace left
        negative = False
        
        # check if valid conversion
        if str[i] != '-' and int(str[i]) not in range(0, 10):
            return 0
        elif str[i] == '-':
            negative = True
            i += 1
        
        for x in range(i, len(str)):
            if int(x) not in range(10):
                break
            int_str += str[x]
        
        print int_str
            
        if negative:
            return int(int_str) * -1
        else:
            return int(int_str)
        