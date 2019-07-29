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
        if headA and headB:
            pA, pB = headA, headB
            while pA != pB:
                pA = pA.next if pA else headB
                pB = pB.next if pB else headA
        return pA
    
