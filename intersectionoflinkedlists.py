# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB # start at the beginning of the linkedlists
        while p1!=p2: # loop through the lists, make sure we're not equal
                        # i.e. we havent found the intersection
            p1=p1.next if p1 else headB # if we're at the end, 
                                # we can't get to it so 
                                # start looping through the next list
                                # and keep going till we get to it
            p2=p2.next if p2 else headA
        return p1
