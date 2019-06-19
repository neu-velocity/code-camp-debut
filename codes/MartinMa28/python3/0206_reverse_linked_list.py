# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        # divide and conquer
        # 1. find the last node of current iteration
        # 2. put the last node in the first place
        # 3. recursively reverse the rest of nodes, 
        #    and connect the first (last previously) node to the reversed nodes
        head_copy = head
        
        while head.next.next:
            head = head.next
        
        last_node = head.next
        head.next = None

        last_node.next = self.reverseList(head_copy)

        return last_node