"""
O(m + n)
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False
            