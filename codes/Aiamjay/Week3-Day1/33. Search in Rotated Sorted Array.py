# encoding=utf-8
class Solution:
    def normal_normal_search(self, nums, target: int) -> int:
        # wjcnote 这个竟然时间更快！
        def worker(begin, end):
            if begin == end:
                return begin if nums[begin] == target else -1
            mid = int((begin + end) / 2)
            if nums[mid] < target:
                return worker(min(mid + 1, end), end)
            else:
                return worker(begin, mid)

        if not nums: return -1
        pivot = 0
        for index in range(1, len(nums)):
            if nums[index - 1] > nums[index]:
                pivot = index
        if target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return worker(0, max(0, pivot - 1))
        else:
            return worker(pivot, len(nums) - 1)

    def general_binary_normal_search(self, nums, target):

        def worker(begin, end):
            # question 如何计算的到中间节点
            if begin == end:
                return begin if nums[begin] == target else -1
            mid = (int((length - begin + end) % length / 2) + begin) % length
            if target > nums[mid]:
                return worker((mid + 1) % length, end)
            else:
                return worker(begin, mid)

        # wjcnote find the pivot
        if not nums: return -1
        pivot = 0
        for index in range(1, len(nums)):
            if nums[index - 1] > nums[index]:
                pivot = index
                break
        length = len(nums)
        return worker(pivot, (length + pivot - 1) % length)

    def test_solution_general_binary_normal_search(self):
        # case 1 normal case without any pivot
        case1 = [1, 2, 3, 4, 5, 6, 7, 8]
        target = 3
        assert self.general_binary_normal_search(case1, target) == 2

        # case 2
        target = 9
        assert self.general_binary_normal_search(case1, target) == -1

        # case 3
        case3 = [1]
        target = 1
        assert self.general_binary_normal_search(case3, target) == 0

        # case 4
        target = 0
        assert self.general_binary_normal_search(case3, target) == -1

        # case 5
        case5 = []
        target = 0
        assert self.general_binary_normal_search(case5, target) == -1

        # case 6
        case6 = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        assert self.general_binary_normal_search(case6, target) == 4

        # case 7
        target = 3
        assert self.general_binary_normal_search(case6, target) == -1

        # case 8
        case8 = [1, 3]
        target = 0
        assert self.general_binary_normal_search(case8, target) == -1

    def test_solution_normal(self):
        # case1
        case1 = [1, 2, 3, 4, 5]
        target = 2
        assert self.normal_search(case1, target) == 1

        # case2
        target = 6
        assert self.normal_search(case1, target) == -1

        # case3
        case3 = [4, 5, 6, 7, 0, 1, 2]
        target = 4
        assert self.normal_search(case3, target) == 0

        # case4
        case3 = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        assert self.normal_search(case3, target) == -1


if __name__ == '__main__':
    s = Solution()
    s.test_solution_general_binary_normal_search()
