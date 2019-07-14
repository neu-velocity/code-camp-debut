# encoding = utf-8
import numpy as np


class Solution:
    def solution(self, obstacleGrid):
        height = len(obstacleGrid)
        if height == 0:
            return 0
        width = len(obstacleGrid[0])
        if width == 0:
            return 1
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * width for _ in range(height)]
        dp[0][0] = 1
        for i in range(1, width):
                dp[0][i] = 0 if obstacleGrid[0][i] == 1 else dp[0][i - 1]
        for i in range(1, height):
            for j in range(width):
                # wjcnote calculate upper and left grid 
                if obstacleGrid[i][j] == 1:
                    # wjcnote A abstacle here
                    dp[i][j] = 0
                else:
                    upper = dp[i - 1][j]
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = upper + left
        return dp[-1][-1]

    def test_solution(self):
        obstacleGrid = [
                          [0,0,0],
                          [0,1,0],
                          [0,0,0],
                       ]
        assert self.solution(obstacleGrid) == 2

        grid = [[]]
        assert self.solution(grid) == 1

        grid = [[0]]
        assert self.solution(grid) == 1

        grid = [[0, 1]]
        assert self.solution(grid) == 0

        grid = [[0],[1]]
        assert self.solution(grid) == 0

        grid = [[1]]
        assert self.solution(grid) == 0
        pass

    def random_test(self):
        candidates = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        m = 20
        n = 16
        grid = np.random.choice(candidates, size=(m, n), replace=True)
        grid[0][0] = grid[-1][-1] = 0
        for item in grid:
            print('[',','.join([str(num) for num in item]),']', end=',')
        print('\n')
        print(self.solution(grid))


if __name__ == "__main__":
    s = Solution()
    s.test_solution()
    # s.random_test()

