class Solution:
    def helper(self, grid, x, y):
        #base case: out of boundary and meet 0
        if x < 0 or x > len(grid) -1 or y < 0 or y > len(grid[0]) -1:
            return
        elif grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.helper(grid, x - 1, y)#left
        self.helper(grid, x + 1, y)#right
        self.helper(grid, x, y + 1)#up
        self.helper(grid, x, y - 1)#down
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.helper(grid, row, col)
                    count += 1
        return count