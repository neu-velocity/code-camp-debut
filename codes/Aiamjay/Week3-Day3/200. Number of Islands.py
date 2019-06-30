import heapq


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        height = len(grid)
        width = len(grid[0])
        if not width:
            return 0
        seen = [[0 for _ in range(width)] for _ in range(height)]
        result = 0

        def explore(row_index, col_index):
            # wjcnote 超出范围
            if row_index == -1 or col_index == -1 or row_index == height or col_index == width:
                return
            # wjcnote 如果这个点是 0(水), 或者之前已经倒过来，直接返回
            if grid[row_index][col_index] == "0" or seen[row_index][col_index] == 1:
                return
            # wjcnote 检查四周
            seen[row_index][col_index] = 1
            # wjcnote 向下探索
            explore(row_index + 1, col_index)
            # wjcnote 向右探索
            explore(row_index, col_index + 1)

        # wjcnote 双层for循环，速度很慢
        for row in range(height):
            for col in range(width):
                if grid[row][col] == "1" and seen[row][col] == 0:
                    result += 1
                    explore(row, col)
        return result

    def numIslands_improved(self, grid):
        width = len(grid[0])
        if not width:
            return 0
        height = len(grid)
        seen = [[0 for _ in range(width)] for _ in range(height)]
        result = 0

        def explore(row_index, col_index):
            if row_index == -1 or col_index == -1 or row_index == height \
                    or col_index == width or seen[row_index][col_index] == 1:
                return 0
            seen[row_index][col_index] = 1
            if grid[row_index][col_index] == "0":
                heapq.heappush(boundary, (row_index, col_index))
                return 0
            explore(row_index + 1, col_index)
            explore(row_index - 1, col_index)
            explore(row_index, col_index + 1)
            explore(row_index, col_index - 1)
            return 1

        # wjcnote 采用最小堆记录边界
        boundary = [(0, 0)]
        while boundary:
            row, col = heapq.heappop(boundary)
            if grid[row][col] == "1":
                result += explore(row, col)
            else:
                result += explore(row, col + 1)
                result += explore(row + 1, col)
        return result

    def test_solution(self):
        # case1
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert self.numIslands_improved(grid) == 1

        # case2
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert self.numIslands_improved(grid) == 3

        # case3
        grid = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]
        ]
        assert self.numIslands_improved(grid) == 1


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
