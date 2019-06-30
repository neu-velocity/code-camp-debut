class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        width = len(matrix[0])
        height = len(matrix)

        # todo 只有一行数据
        def dfs(row, col, last, seen):
            if row == -1 or row == height \
                    or col == -1 or col == width \
                    or seen[row][col] == 1 \
                    or matrix[row][col] < last:
                return []
            seen[row][col] = 1
            return dfs(row + 1, col, matrix[row][col], seen) + \
                   dfs(row - 1, col, matrix[row][col], seen) + \
                   dfs(row, col + 1, matrix[row][col], seen) + \
                   dfs(row, col - 1, matrix[row][col], seen) + \
                   [(row, col)]

        # to pacific:
        pacific_seen = [[0] * width for _ in range(height)]
        pacific = []
        atlantic_seen = [[0] * width for _ in range(height)]
        atlantic = []

        for index in range(width):
            if not pacific_seen[0][index]:
                pacific += dfs(0, index, matrix[0][index], pacific_seen)
            if not atlantic_seen[height - 1][index]:
                atlantic += dfs(height - 1, index, matrix[height - 1][index], atlantic_seen)

        for index in range(height):
            if not pacific_seen[index][0]:
                pacific += dfs(index, 0, matrix[index][0], pacific_seen)
            if not atlantic_seen[index][width - 1]:
                atlantic += dfs(index, width - 1, matrix[index][width - 1], atlantic_seen)
        return list(set(pacific).intersection(atlantic))

    def test_solution(self):
        matrix = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        print(sorted(self.pacificAtlantic(matrix)))

        matrix = [
            [3, 3, 3],
            [3, 1, 3],
            [0, 2, 4]
        ]
        print(sorted(self.pacificAtlantic(matrix)))
        # [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        matrix = [
            [1, 2],
            [4, 3]]
        print(sorted(self.pacificAtlantic(matrix)))


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
