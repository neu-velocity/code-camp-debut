# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
solution1: Similar to LC141 solution 1
but won't work for the follow up
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        record = []
        while head and head.next:
            if head in record:
                return head
            record.append(head)
            head = head.next
        return None

"""
solution2: when slow and fast meet, set one of pointers to head
when two pointers meet again, they are at the cycle starting node
"""
    def detectCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow is fast:
                temp = head
                while temp is not slow:
                    temp = temp.next
                    slow = slow.next
                return slow
        
        return None
