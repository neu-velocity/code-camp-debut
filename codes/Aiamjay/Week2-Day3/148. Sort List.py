# encoding = utf-8
from codes.Aiamjay.utils.linked_list_utils import *
import timeit


class Solution1:
    def sortList(self, head):
        if not head or not head.next:
            return head
        new_head, _ = self.quick_sort_iterative(head)
        return new_head

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

    def quick_sort_recursive(self, head):
        # 递归的返回条件
        if not head or not head.next:
            return head, head
        pivot_list = pivot_cur = head
        left_list = left_cur = ListNode(0)
        right_list = right_cur = ListNode(0)
        temp = head
        while temp.next:
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
        pivot_cur.next = None
        left_cur.next = None
        right_cur.next = None

        left_beg, left_end = self.quick_sort_recursive(left_list.next)
        if left_beg:
            left_end.next = pivot_list
        else:
            left_beg = pivot_list
        right_beg, right_end = self.quick_sort_recursive(right_list.next)
        # right_end返回不能为空
        if right_end:
            pivot_cur.next = right_beg
        else:
            right_end = pivot_cur

        return left_beg, right_end


class Solution2(object):
    def sortList_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        self.quick_sort_recursive(head, None)
        return head

    def quick_sort_recursive(self, head, tail):
        # python版本的链表快排，堆栈递归版本
        middle = self.partition(head, tail)
        if not (middle is head or middle is head.next):
            self.quick_sort_recursive(head, middle)
        if not (middle is tail or middle.next is tail):
            self.quick_sort_recursive(middle.next, tail)

    def sortList(self, head):
        if not head or not head.next:
            return head
        return self.quick_sort_iterative(head)

    def quick_sort_iterative(self, h):
        new_head = ListNode(0)
        new_head.next = h
        a = [new_head, None]
        while a:
            tail = a.pop()
            head = a.pop()
            par_head, par_end = self.partition_improved(head, tail)
            if not (head.next is par_head or head.next.next is par_head):
                a += [head, par_head]
            if not (par_end.next is tail or par_end.next.next is tail):
                a += [par_end, tail]
        return new_head.next

    # 首位只是用来方便首尾相连，并不是用作排序
    # 最终还是没有imoroved 耗时还是很长。没有原来的方法效率高
    def partition_improved(self, head, tail):
        pivot = head.next
        pivot_head = head.next
        temp = head.next.next
        list_less, list_great = ListNode(0), ListNode(0)
        list_less_cur, list_great_cur = list_less, list_great
        while temp is not tail:
            if pivot.val > temp.val:
                list_less_cur.next = temp
                list_less_cur = list_less_cur.next
            elif pivot.val < temp.val:
                list_great_cur.next = temp
                list_great_cur = temp
            else:
                pivot.next = head
                pivot = head
            temp = temp.next
        if list_less.next:
            head.next = list_less.next
            list_less_cur.next = pivot_head
        if list_great.next:
            pivot.next = list_great.next
            list_great_cur.next = tail
        else:
            pivot.next = tail

        return pivot_head, pivot

    def partition(self, head, tail):
        pivot = head
        location = head
        head = head.next
        while head != tail:
            if head.val < pivot.val:
                location = location.next
                head.val, location.val = location.val, head.val
            head = head.next
        pivot.val, location.val = location.val, pivot.val
        return location


if __name__ == '__main__':
    a = [2, 3, 1, 4, 2, 10, 3, 2, 1, 2, 1, 2, 3, 4, 5, 5, 6, 4, 2, 2, 4, 5, 6, 4, 3, 3, 3]
    a = list_to_linked_list(a)
    print_link_list(a)
    b = Solution1()
    start = timeit.default_timer()
    head = b.sortList(a)
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    print_link_list(head)
