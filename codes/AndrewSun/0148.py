# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # if the linked list has only one node
        if not head or not head.next: 
            return head
        # fast and slow pointers to find the median of the list
        mid, slow, fast = head, head, head
        while fast and fast.next:
            mid = slow;
            slow = slow.next
            fast = fast.next.next
        # cut the list from the middle
        mid.next = None
        # sort the sublist recursively
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        # merge the two parts
        return self.mergeLists(l1, l2)
    
    def mergeLists(self, l1, l2):
        # initialize a dummy head
        head = ListNode(-1)
        # cur -> the current node
        cur = head
        if not l1:
            return l2
        elif not l2:
            return l1
        # merge the elements in ascending order
        else:
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            # link the remaining part
            cur.next = l1 if l1 else l2
            # return the real head of the linked list
            return head.next