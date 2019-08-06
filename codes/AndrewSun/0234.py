# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        rev = None # the head point of the first reversed half 
        while(fast and fast.next):
            fast = fast.next.next
            # Reverse the first half of the linked list
            rev, rev.next, slow = slow, rev, slow.next
        # if the number of elements is odd, move the slow pointer one step
        if fast:
            slow = slow.next
        # Compare the first half with the second half
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev
            
        