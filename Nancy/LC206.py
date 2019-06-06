# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iterative
        node = None
        while head:
            temp_next = head.next
            head.next = node
            node = head
            head = temp_next
        return node

"""
好吧。。。没看懂recursion解法
“”“