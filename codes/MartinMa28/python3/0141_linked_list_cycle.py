class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
            
        one_step = head
        two_step = head
        while one_step.next and two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step is two_step:
                return True


        return False


if __name__ == "__main__":
    ln1 = ListNode(3)
    ln1.next = ListNode(2)
    ln1.next.next = ListNode(0)
    ln1.next.next.next = ListNode(-4)
    ln1.next.next.next.next = ln1.next

    solu = Solution()
    print(solu.hasCycle(ln1))