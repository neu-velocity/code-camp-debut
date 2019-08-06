"""
O(log(m) + log(n)) = O(log(mn))
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        return self.findCol(matrix, self.findRow(matrix,target), target)
        
    def findRow(self, matrix, target):    
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + (r - l)//2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                return m
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False
    
    def findCol(self, matrix, m, target):
        l = 0
        r = len(matrix[m]) - 1
            
        while l + 1 < r:
            mid = l + (r - l)//2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                r = mid
            else:
                l = mid
            
        if matrix[m][l] == target or matrix[m][r] == target:
            return True

        return False
            