# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while (m - 1):
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        M_ = prev
        M = cur
        
        while (n - 1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
            n -= 1
        N = prev
        N_ = cur
        M.next = N_
        M_.next = N