# Definition for singly-linked list.
from codes.Aiamjay.utils.linked_list_utils import *


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2

        def helper(head, p1, p2):
            while p1 and p2:
                if p1.val < p2.val:
                    head.next, p1 = ListNode(p1.val), p1.next
                elif p1.val > p2.val:
                    head.next, p2 = ListNode(p2.val), p2.next
                else:
                    head.next, p1 = ListNode(p1.val), p1.next
                    head = head.next
                    head.next, p2 = ListNode(p2.val), p2.next
                head = head.next
            head.next = p1 if p1 else p2

        if l1.val < l2.val:
            new_head = ListNode(l1.val)
            helper(new_head, l1.next, l2)
        else:
            new_head = ListNode(l2.val)
            helper(new_head, l1, l2.next)
        return new_head


if __name__ == '__main__':
    a = list_to_linked_list([1, 2, 3, 4])
    b = list_to_linked_list([2, 3, 4, 5, 6])
    s = Solution()
    print_link_list(s.mergeTwoLists(a, b))
