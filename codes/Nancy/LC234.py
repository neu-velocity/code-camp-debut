# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Solution1:
Go through and record every node in a stack
Then start from the beginning of the linked list,
compare with stack.top()

Note: won't work for the follow up since space is O(n)
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        while len(stack) > 0:#two pointer will work as well
            if head.val == stack[-1]:
                stack.pop()
            else:
                return False
            head = head.next
        return True

"""
Solution2: follow up
Locate the mid node, reverse the second half
compare it with the first half
贼喜欢这个解hhhh
"""   

        def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #locate the mid node
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half
        node = None
        while slow:
            temp_next = slow.next
            slow.next = node
            node = slow
            slow = temp_next
        
        #let's compare
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
        
