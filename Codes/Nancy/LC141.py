# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Solution 1: record each head as you move to the next, and check if current head has been
added to the list

Note: Space is O(n), won't work for the follow up
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        record = []
        
        while head:
            if head in record:
                return True
            record.append(head)
            head = head.next
        return False


"""
Follow up: O(1) memory?

Two pointers:
the fast pointer is 1 step ahead of the slow pointer: 
as the slow pointer moves 1 step, the fast moves 2 steps 
Two pointers will meet up eventually if the linked list has a cycle in it
不知道要做多少遍才能想到这个方法LOL
"""

    def hasCycle_2(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False