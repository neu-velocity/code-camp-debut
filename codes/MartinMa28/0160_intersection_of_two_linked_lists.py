class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None) or (headB is None):
            return None

        tempA = headA
        tempB = headB

        # get the length of A and B
        lenA = 0
        lenB = 0

        while tempA:
            lenA += 1
            tempA = tempA.next
        
        while tempB:
            lenB += 1
            tempB = tempB.next

        # find the node after which both of the linked lists have
        # the same amount of nodes
        diff = lenA - lenB

        if diff > 0:
            for _ in range(diff):
                headA = headA.next
        
        elif diff < 0:
            for _ in range(-diff):
                headB = headB.next

        # check whether A and B have the same (intersected) node
        while headA:
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        

        return None
        