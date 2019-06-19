"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        nodes_mappings = {}
        head_copy = head
        
        header = Node(-999, None, None)
        header_copy = header
        while head:
            header.next = Node(head.val, None, None)
            nodes_mappings[head] = header.next
            head = head.next
            header = header.next

        head = head_copy
        header = header_copy
        while head:
            header.next.random = nodes_mappings.get(head.random, None)
            head = head.next
            header = header.next

        return header_copy.next


if __name__ == "__main__":
    node2 = Node(2, None, None)
    node2.random = node2
    node1 = Node(1, node2, node2)

    solu = Solution()
    print(solu.copyRandomList(node1))