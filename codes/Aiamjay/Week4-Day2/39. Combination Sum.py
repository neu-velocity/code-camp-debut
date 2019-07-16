# encoding = utf-8
from collections import deque


class Solution:

    def combinationSum(self, candidates: list, target: int):
        candidates = sorted([item for item in candidates if item <= target])
        return self.backtracking(candidates, target)

    @staticmethod
    def backtracking(nums: list, target):
        result = []
        stack = deque()
        stack.append((0, 0, []))
        while stack:
            cur_index, cur_sum, path = stack.pop()
            if cur_index < len(nums) and nums[cur_index] != 0 and target - cur_sum >= nums[cur_index]:
                for index in range((target - cur_sum) // nums[cur_index] + 1):
                    stack.append((cur_index + 1,
                                  cur_sum + index * nums[cur_index],
                                  path + [nums[cur_index]] * index))

            else:
                if cur_sum == target:
                    result.append(path)
                continue
        return result

    def test_solution(self):
        # case 1
        print("case 1")
        candidates = [2, 3, 6, 7]
        target = 7
        for item in self.combinationSum(candidates, target):
            print(item)

        # case 2
        print("case 2")
        candidates = [2, 3, 5]
        target = 8
        for item in self.combinationSum(candidates, target):
            print(item)


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
