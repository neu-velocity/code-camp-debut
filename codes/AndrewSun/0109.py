# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        fast = slow = head
        # Edge Condition
        if not head: 
            return head
        elif not head.next:
            root = TreeNode(head.val)
            return root
        
        # find the middle of the linked list
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        # Disconnect the left portion of the tree
        prev.next = None
        # Recursive 
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(slow.next)
        root = TreeNode(slow.val)
        root.left = left
        root.right = right
        
        return root
        