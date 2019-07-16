# encoding = utf-8
import numpy as np


class Solution:
    def solution(self, nums):
        length = len(nums)
        if length < 2:
            return True
        dp = [0] * length
        dp[0] = nums[0]
        for i in range(1, length):
            flag = False
            for j in range(i - 1, -1, -1):
                if i <= dp[j]:
                    dp[i] = i + nums[i]
                    if dp[i] >= length - 1:
                        return True
                    flag = True
                    break
            if not flag:
                return False
        return True

    def test_solution(self):
        nums = [0]
        print(self.solution(nums))

        nums = [1]
        print(self.solution(nums))

        nums = [2,3,1,1,4]
        print(self.solution(nums))

        nums = [3,2,1,0,4]
        print(self.solution(nums))

        nums = [1, 1, 1, 1, 1, 1, 1]
        print(self.solution(nums))

    def random_test(self):
        candidates = range(5)
        nums = np.random.choice(candidates, size = 12, replace=True)
        print('[', ','.join([str(item) for item in nums]), ']')
        print(self.solution(nums))

if __name__ == "__main__":
    s = Solution()
    s.test_solution()
    s.random_test()


