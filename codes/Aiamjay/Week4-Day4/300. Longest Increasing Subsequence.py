# encoding = utf-8
import numpy as np


class Solution:
    def solution(self, nums: list):
        length = len(nums)
        if length < 2:
            return length
        dp = [1] * length
        ans = 1
        for i in range(1, length):
            cur_num = nums[i]
            for j in range(i - 1, -1, -1):
                # wjcnote find the num that is smaller than current
                if nums[j] < cur_num:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans

    def test_solution(self):
        # wjcnote corner case test
        nums = []
        print(self.solution(nums))

        nums = [2]
        print(self.solution(nums))

        # wjcnote failed cases
        nums = [2, 2]
        print(self.solution(nums))

    def random_test(self):
        candidates = range(20)
        nums = np.random.choice(candidates, size=10, replace=True)
        print('[',','.join([str(item) for item in nums]), ']')
        print(self.solution(nums))
        pass

if __name__ == "__main__":
    s = Solution()
    s.test_solution()
    s.random_test()

