# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # use a list as a stack of elements that we've seen
        self.stack=[]
        stack.append(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        # base case, that there is a left node 
        while(stack[-1].left!=None):
            stack.append(stack[-1].left) # add this to the stack
        
        # at the end of this, we'll have the minimum value in our stack
        
        leftmost=stack.pop()
        stack[-1].left=None # so we don't continue down that line anymore
        return leftmost.val
    
        # case we just popped and now we have an element w a right branch
        if stack[-1]
        
            
            
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()