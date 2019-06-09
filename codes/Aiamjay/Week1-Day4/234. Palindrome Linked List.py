# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        def get_length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        length = get_length(head)

        def reverse_move(head, l):
            first = head
            second = first.next
            while l:
                l -= 1
                temp = second.next
                second.next = first
                first = second
                second = temp
            return first, second if length % 2 == 0 else second.next

        h1, h2 = reverse_move(head, length / 2 - 1)
        head.next = None
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True


