from codes.Aiamjay.utils.linked_list_utils import *


class Solution1(object):
    # 使用快排
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def to_end(head):
            while head.next:
                head = head.next
            return head

        lists = [item for item in lists if item]
        if not lists: return None
        head = lists[0]
        end = to_end(head)
        for l in lists[1:]:
            end.next = l
            end = to_end(l)
        head, _ = self.quick_sort_iterative(head)
        return head

    def quick_sort_iterative(self, head):
        new_head = ListNode(0)
        new_head.next = head
        a = [new_head, None]
        while a:
            end = a.pop()
            beg = a.pop()
            middle_beg, middle_end = self.partition_iterative(beg, end)
            if not (beg.next is middle_beg or beg.next.next is middle_beg):
                a += [beg, middle_beg]
            if not (middle_end.next is end or middle_end.next.next is end):
                a += [middle_end, end]

        return new_head.next, None

    def partition_iterative(self, head, tail):
        pivot_list = pivot_cur = head.next
        left_list = left_cur = ListNode(0)
        right_list = right_cur = ListNode(0)

        temp = pivot_cur
        while temp.next is not tail:
            temp = temp.next
            if temp.val < pivot_cur.val:
                left_cur.next = temp
                left_cur = temp
            elif temp.val > pivot_cur.val:
                right_cur.next = temp
                right_cur = temp
            else:
                pivot_cur.next = temp
                pivot_cur = temp

        if left_list.next:
            head.next = left_list.next
            left_cur.next = pivot_list
        else:
            head.next = pivot_list
        if right_list.next:
            pivot_cur.next = right_list.next
            right_cur.next = tail
        else:
            pivot_cur.next = tail

        return pivot_list, pivot_cur


class Solution2:
    # brute force
    def mergeKLists(self, lists):
        new_head = temp = self.get_smallest_in_k(lists)
        lists.remove(temp)
        if temp.next:
            lists.append(temp.next)
        while lists:
            smallest = self.get_smallest_in_k(lists)
            temp.next = smallest
            temp = smallest
            lists.remove(smallest)
            if smallest.next:
                lists.append(smallest.next)
        return new_head

    def get_smallest_in_k(self, lists):
        smallest = lists[0]
        for item in lists[1:]:
            if item.val < smallest.val:
                smallest = item
        return smallest


class Solution2:
    def mergeKLists(self, lists):
        while len(lists) != 1:
            cur_len = len(lists)
            half = cur_len // 2
            for i in range(half):
                l = self.merge_two_lists(lists[i], lists[i + half])
                lists.append(l)
            if cur_len % 2 != 0:
                lists.append(lists[cur_len - 1])
            lists = lists[cur_len:]
        return lists[0]

    def merge_two_lists(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2

        def helper(head, p1, p2):
            while p1 and p2:
                if p1.val < p2.val:
                    head.next = p1
                    p1 = p1.next
                elif p1.val > p2.val:
                    head.next = p2
                    p2 = p2.next
                else:
                    head.next = p1
                    p1 = p1.next
                    head = head.next
                    head.next = p2
                    p2 = p2.next
                head = head.next
            if p1:
                head.next = p1
            if p2:
                head.next = p2

        if l1.val < l2.val:
            new_head = l1
            helper(new_head, l1.next, l2)
        else:
            new_head = l2
            helper(new_head, l1, l2.next)
        return new_head


if __name__ == '__main__':
    a = [
        [3, 4, 5],
        [5, 6, 7, 8],
        [1, 3, 5, 7, 9],
        [7, 9, 10, 12, 14]
    ]
    lists = lists_to_lists_of_linked_list(a)
    s = Solution2()
    head = s.mergeKLists(lists)
    # head = s.merge_two_lists(lists[0], lists[1])
    print_link_list(head)
