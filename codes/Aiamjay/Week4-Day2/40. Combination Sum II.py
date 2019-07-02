# encoding = utf-8
from collections import deque


class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        return self.backtracking(sorted([num for num in candidates if num <= target]), target)

    def backtracking(self, nums, target):
        result = []
        stack = deque()
        stack.append((0, 0, sum(nums), []))
        while stack:
            cur_index, cur_sum, left_sum, path = stack.pop()
            if cur_sum == target:
                result.append(path)
                continue
            if cur_index == len(nums) or \
                    left_sum + cur_sum < target or \
                    cur_sum > target or \
                    target - cur_sum < nums[cur_index]:
                continue
            # wjcnote 这里有优化，当后面一个元素和当前的元素相等的时候
            # wjcnote 如果当前元素不计算入内，则不需要考虑后面一个元素，直接跳到与当前元素不想等的元素上
            temp = cur_index + 1
            while temp < len(nums) and nums[temp] == nums[cur_index]:
                temp += 1
            if temp < len(nums):
                stack.append((temp,
                              cur_sum,
                              left_sum - nums[cur_index],
                              path))
            # wjcnote 当前元素计算入内，一律全部入栈
            stack.append((cur_index + 1,
                          cur_sum + nums[cur_index],
                          left_sum - nums[cur_index],
                          path + [nums[cur_index]]))
        return result

    def test_solution(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        for item in self.combinationSum2(candidates, target):
            print(item)


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
