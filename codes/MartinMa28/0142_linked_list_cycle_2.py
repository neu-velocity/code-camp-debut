# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        visited = []
        
        while head is not None:
            if head in visited:
                return head
            visited.append(head)
            head = head.next
        return None


if __name__ == "__main__":
    test_head = ListNode(3)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(0)
    test_head.next.next.next = ListNode(-4)
    test_head.next.next.next.next = test_head.next

    solu = Solution()
    print(solu.detectCycle(test_head))