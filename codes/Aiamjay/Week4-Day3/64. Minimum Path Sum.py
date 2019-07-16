# encoding = utf-8
from math import inf


class Solution:
    def minPathSum(self, grid) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        if num_col == 0:
            return 0
        dp = [[0] * num_col for _ in range(num_row)]
        dp[0][0] = grid[0][0]
        for col in range(1, num_col):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
        for row in range(1, num_row):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for row in range(1, num_row):
            for col in range(1, num_col):
                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + grid[row][col]
        for row in dp:
            print(row)
        return dp[-1][-1]

    def test_solution(self):
        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        print(self.minPathSum(grid))

        grid = [[1, 2, 3]]
        print(self.minPathSum(grid))
        pass


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
