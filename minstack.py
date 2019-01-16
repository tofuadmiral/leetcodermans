class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # get an item onto the stack 
        self.list.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        poppedelement=self.list[-1]
        del self.list[len(self.list)-1]
        return poppedelement
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()