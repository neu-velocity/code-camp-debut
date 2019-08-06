# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        l = r = head
        while True:
            count = 0
            while r and count < k:
                r =r.next
                count += 1
            if count == k:
                cur, prev = l, r
            # Standard reverse
                for _ in range(k):
                    cur.next, prev, cur = prev, cur, cur.next
                jump.next, jump, l = prev, l, r 
            else:
                return dummy.next
            
                
                
        