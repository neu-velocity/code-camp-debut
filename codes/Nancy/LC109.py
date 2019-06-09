# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time O(nlogn)
it takes N/2 steps to find the middle of a linked list with NN elements. 
After finding the middle element, we are left with two halves of size N/2 each. 
Then, we find the middle element for both of these halves and it would take a total of 2 * N/4 steps for that. 
And similarly for the smaller sublists that keep forming recursively. 
"""
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        if head.next == None: #只有一个head的时候，slow&fast both = None
            return TreeNode(head.val)
        
        slow = head
        fast = head
        last = slow
        while fast and fast.next:
            last = slow #record the position right before slow
            slow = slow.next
            fast = fast.next.next
        
        node = TreeNode(slow.val)
        
        last.next = None #cut off the first half of the linked list
        scd_first = slow.next #set up the second half starting node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(scd_first)
        return node