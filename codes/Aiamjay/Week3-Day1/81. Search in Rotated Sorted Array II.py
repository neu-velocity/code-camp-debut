# encoding=utf-8
"""wjcnote 这个题目和33是整体上是一样，区别在于这个题目允许出现相同的元素"""


class Solution:
    def search(self, nums, target: int) -> bool:
        def worker(begin, end):
            # question 如何计算的到中间节点
            if begin == end:
                return True if nums[begin] == target else False
            mid = (int((length - begin + end) % length / 2) + begin) % length
            if target > nums[mid]:
                return worker((mid + 1) % length, end)
            else:
                return worker(begin, mid)

        # wjcnote find the pivot
        if not nums: return False
        pivot = 0
        for index in range(1, len(nums)):
            if nums[index - 1] > nums[index]:
                pivot = index
                break
        length = len(nums)
        return worker(pivot, (length + pivot - 1) % length)

    def search_improved(self, nums, target) -> bool:
        def worker(begin, end):
            # wjcnote 区别在这句话
            # wjcnote 由于定位的区间都确保是单调区间，所以如果出现首尾相等情况，则可以跳过区间
            if begin == end or nums[begin] == nums[end]:
                return True if nums[begin] == target else False
            mid = (int((length - begin + end) % length / 2) + begin) % length
            if target > nums[mid]:
                return worker((mid + 1) % length, end)
            else:
                return worker(begin, mid)

        if not nums:
            return False
        pivot = 0
        for index in range(1, len(nums)):
            if nums[index - 1] > nums[index]:
                pivot = index
                break
        length = len(nums)
        return worker(pivot, (length + pivot - 1) % length)
