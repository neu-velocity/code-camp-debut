class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def sortList(self, head):
        if head is None:
            return None

        if head.next is None:
            return head

        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1

        mid = length // 2

        cur = head
        for _ in range(mid - 1):
            cur = cur.next
        
        sec_half = cur.next
        cur.next = None

        return self.mergeTwoLists(self.sortList(head), self.sortList(sec_half))

        
        
