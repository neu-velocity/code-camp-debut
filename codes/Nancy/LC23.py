# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Brute Force:
merge sort 2 linked lists until we have gone through all linked lists in the lists
Assume k elements in lists
N nodes in the final linked list
time complexity: O(kN)
"""
class Solution:
    def mergeSort(self, l1, l2):
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
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
            
        return dummy.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return lists
        
        cur = self.mergeSort(lists[0],lists[1])
        i = 2
        while i < len(lists):
            cur = self.mergeSort(cur, lists[i])
            i += 1
        return cur

"""
Divide & Conquer
Don't understand why this is better in terms of time complexity
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeSort(self, l1, l2):
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
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
            
        return dummy.next
    
    """
    Divide and conquer
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return lists
        n = len(lists)
        interval = 1
        while interval < n:
            i = 0
            while i < n - interval:
                lists[i] = self.mergeSort(lists[i], lists[i + interval])
                i += 2 * interval #a bit hard to think
            interval *= 2 #a bit hard to think
        return lists[0]

