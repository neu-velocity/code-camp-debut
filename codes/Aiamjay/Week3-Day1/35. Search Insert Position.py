# encoding=utf-8


class Solution:

    @staticmethod
    def searchInsert(nums, target: int) -> int:
        def binary_search(begin, end):
            if begin == end:
                return begin if target < nums[begin] else begin + 1 if target > nums[begin] else begin
            mid = int((begin + end) / 2)
            if target == nums[mid]:
                return mid
            else:
                return binary_search(begin, max(0, mid - 1)) if target < nums[mid] else \
                    binary_search(min(mid + 1, end), end)

        if not nums:
            return 0
        return binary_search(0, len(nums) - 1)


def test_solution():
    s = Solution()
    # case 1
    case1 = [1, 3, 4]
    target = 2
    assert s.searchInsert(case1, target) == 1
    # case 2
    case2 = []
    target = 1
    assert s.searchInsert(case2, target) == 0
    # case3
    case3 = [1]
    target = 2
    assert s.searchInsert(case3, target) == 1
    # case4
    case4 = [1, 3, 5, 6]
    target = 5
    assert s.searchInsert(case4, target) == 2
    # case5
    case5 = [1, 3]
    target = 0
    assert s.searchInsert(case5, target) == 0
    # case6
    case6 = [1, 3]
    target = 5
    assert s.searchInsert(case6, target) == 2
    # case7
    case7 = [1]
    target = 1
    assert s.searchInsert(case7, target) == 0
    # case8
    case8 = [1, 3]
    target = 2
    assert s.searchInsert(case8, target) == 1


if __name__ == '__main__':
    test_solution()
