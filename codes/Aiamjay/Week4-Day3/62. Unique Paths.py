# encoding = utf-8


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]
        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]

    def formula(self, m, n) -> int:
        total_steps = m + n - 2
        down_steps = n - 1
        # wjcnote the ans is C(total_steps, down_steps)  C=combination组合
        ans = 1
        for i in range(1, down_steps):
            ans *= (total_steps - down_steps + i) / i
        return int(ans)

    def test_solution(self):
        # case 1
        print(self.uniquePaths(7, 3))

        # corner case
        print(self.uniquePaths(1, 1))

        # corner case
        print(self.uniquePaths(1, 10))
        pass


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
