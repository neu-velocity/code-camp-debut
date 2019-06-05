class Solution(object):
    """
    Solution 1
    Go through both linked lists, get the length difference
    Set the starting point of the longer linked list at head+diff
    """
    
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        len_A = 0
        len_B = 0
        nodeA = headA
        nodeB = headB
        
        while nodeA or nodeB:
            if nodeA == nodeB:
                return nodeA
            
            if nodeA:
                len_A += 1
                nodeA = nodeA.next
            
            if nodeB:
                len_B += 1
                nodeB = nodeB.next
        
        diff = abs(len_A - len_B)
        if len_A > len_B:
            i = diff
            while i != 0:
                headA = headA.next
                i -= 1
        else:
            i = diff
            while i != 0:
                headB = headB.next
                i -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
    
    """
    Solution 2: two pointers
    len_A + len_B = X, X is constant for each case
    The goal here is to let both pointers go through same length by 
    swiching starting point
    居然有点喜欢这个“反人类”的解法
    """
    def getIntersectionNode(self, headA, headB):
        nodeA = headA
        nodeB = headB
        
        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        
        return nodeA

