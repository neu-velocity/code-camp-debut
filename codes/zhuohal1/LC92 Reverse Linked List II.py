# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        if m > 1:
            new_head = head
            new_head.next = self.reverseBetween(head.next, m-1, n-1)
            return new_head
        else:
            new_next = head.next
            new_head = self.reverseBetween(new_next, 1, n-1)
            new_rest = new_next.next
            new_next.next = head
            head.next = new_rest
            return new_head