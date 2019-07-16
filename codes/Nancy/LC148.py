# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Merge Sort
- Find the mid node of the linked list
- merge two <b>SORTED</b> left and right linked list using recursion
"""

class Solution:
    def mergeSort(self,l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        #in case of non-equal length
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
        
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        pre = slow = fast = head
        while fast != None and fast.next != None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        #slow is the mid node
        #pre is the one b/f the mid
        pre.next = None #break apart
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.mergeSort(left, right)
