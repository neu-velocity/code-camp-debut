# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        step_1 = head
        step_2 = head

        while True:
            if step_2 and step_2.next:
                step_1 = step_1.next
                step_2 = step_2.next.next

                if step_2:
                    if step_1 is step_2:
                        return True
            
            else:
                return False