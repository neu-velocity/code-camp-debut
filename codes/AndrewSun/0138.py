"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        cur = head
        # Duplicate the origin list
        while cur:
            new = Node(cur.val, None, None)
            cur.next, new.next, cur = new, cur.next, cur.next
        
        # Copy the random point 
        cur = head
        while cur:
            cur.next.random, cur  = cur.random.next, cur.next.next
        # Extracted the copyed list
        cur = head
        newHead = head.next
        while cur.next.next:
            cur.next, cur.next.next = cur.next.next, cur.next.next.next

        return newHead