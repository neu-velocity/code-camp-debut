# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True