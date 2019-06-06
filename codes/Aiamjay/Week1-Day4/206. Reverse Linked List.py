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
        # iteratively
        if not head or not head.next:
            return head
        first = None
        second = head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        return first

    def reverseList2(self, head):
        # recursively
        if not head:
            return head

        def helper(list_head):
            if not list_head.next:
                helper.head = list_head
                return list_head
            helper(list_head.next).next = list_head
            return list_head

        helper(head).next = None
        return helper.head
