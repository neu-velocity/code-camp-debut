# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 退出条件
        if k == 0 or k == 1:
            return head

        def get_length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        length = get_length(head)

        def reverse(head, l):
            first = head
            second = head.next
            while l:
                temp = second.next
                second.next = first
                first = second
                second = temp
                l -= 1
            return first, second

        n = length / k
        begin = head
        last = None
        for i in range(n):
            first, second = reverse(begin, k - 1)
            if i == 0:
                head = first
            else:
                last.next = first
            last = begin
            begin.next = second
            begin = second
        return head




