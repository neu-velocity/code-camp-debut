# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return head

        def to_left(head, m):
            while m > 1:
                head = head.next
                m -= 1
            return head

        def reverse_list(head, length):
            first = head
            second = first.next
            while length:
                temp = second.next
                second.next = first
                first = second
                second = temp
                length -= 1
            return first, second

        left_sec = to_left(head, m - 1)
        first, second = reverse_list(head if m == 1 else left_sec.next, n - m)

        if m == 1:
            left_sec.next = second
            return first
        else:
            temp = left_sec.next
            left_sec.next = first
            temp.next = second
            return head

