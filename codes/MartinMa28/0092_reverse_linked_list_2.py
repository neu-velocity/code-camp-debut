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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head is None:
            return None
        
        # add a header before any non-trivial node
        header = ListNode(-999)
        header.next = head
        head = header

        index = 0
        while head:
            if index == m - 1:
                before_reverse = head
                start = head.next
            if index == n:
                end = head
                after_reverse = head.next
                break
            
            index += 1
            head = head.next

        end.next = None
        reversed_linked_list = self.reverseList(start)
        before_reverse.next = reversed_linked_list

        head = header
        while head.next:
            head = head.next
        
        head.next = after_reverse

        return header.next
