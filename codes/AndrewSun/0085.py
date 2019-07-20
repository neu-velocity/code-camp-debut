class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = [0] * n
        right = [n - 1] * n
        height = [0] * n
        maxArea = 0
        for i in range(m):
            leftBound = 0 # the index of the leftmost element of the current row
            rightBound = n - 1 # the index of the rightmost element of the current row

            # Update the height (the same concept of bar in "largest area of histogram")
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # Left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], leftBound) #this means the current boundry should satisfy two conditions: within the boundry of the previous height array, and within the boundry of the current row
                else:
                    left[j] = 0 # reset the left to 0, for calculating left[i+1][j] in the next row
                    leftBound = j + 1 # update the left bound of the current row
            # Right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], rightBound)
                else:
                    right[j] = n - 1
                    rightBound = j - 1

            # Calculate the max area
            for j in range(n):
                maxArea = max(maxArea, (right[j] - left[j] + 1) * height[j])
        return maxArea

m = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(Solution().maximalRectangle(m))
            