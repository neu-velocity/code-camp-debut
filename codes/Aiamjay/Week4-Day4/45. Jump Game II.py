# encoding = utf-8
from math import inf
import numpy as np


class Solution:
    def solution(self, nums):
        """dp solution
        although I optimized this algorithm, it still falied to past the last
        two cases (the worest cases).
        This problem is not intended to be solved by dp solution.
        """
        length = len(nums)
        if length < 2:
            return 0
        dp = [inf] * length
        dp[0] = 0
        for i in range(1, length):
            flag = False
            for j in range(i, 0, -1):
                if j <= nums[i - j]:
                    dp[i] = min(dp[i], dp[i - j] + 1)
                    flag = True
                    break
            if not flag:
                return 0
        return dp[-1]

    def test_solution(self):
        nums = [2,3,1,1,4]
        print(self.solution(nums))

        candidates = range(20)
        nums = np.random.choice(candidates, size = 40, replace=True)
        print('[',','.join([str(item) for item in nums]),']')
        print(self.solution(nums))
        pass


if __name__ == "__main__":
    s = Solution()
    s.test_solution()

