class Solution:
    def numIslands(self, grid) -> int:
        # recursive function 
        def dfs (i, j):
            for u, v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if check(u, v):
                    grid[u][v] = '#'
                    dfs(u, v)
        # check if the node is valid/matched
        def check(i, j):
            if (i < 0) or (i > len(grid) - 1) or (j< 0) or (j > len(grid[0]) - 1) or grid[i][j] != '1':
                return False
            else:
                return True
        # main part
        # the null input   
        if not grid:
            return 0
        # the number of the island 
        ans = 0
        # traverse each node in the grid(matrix)
        # the number of the islands is the number of DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    # change this node into '#'
                    grid[i][j] == '#'
                    # DFS -> turn all the nodes of the same island into '#'
                    dfs(i, j)
        return ans
            
Input = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
test = Solution()
print(test.numIslands(Input))
