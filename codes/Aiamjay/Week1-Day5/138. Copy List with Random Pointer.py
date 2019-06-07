"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        cache = {}

        def copy(origin):
            if origin not in cache:
                cache[origin] = Node(origin.val, origin.next, origin.random)
            return cache[origin]

        def copy_next(head):
            while head.next:
                head.next = copy(head.next)
                head = head.next
            head.next = None

        def copy_random(head):
            while head:
                head.random = copy(head.random) if head.random else None
                head = head.next

        new_head = copy(head)
        copy_next(new_head)
        copy_random(new_head)
        return new_head
