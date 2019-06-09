# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next

        for i in range(len(nodes) // 2):
            if nodes[i] != nodes[len(nodes) - 1 - i]:
                return False
        
        return True
