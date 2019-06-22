class Solution:
    def binary_search(self, nums: list, target: int) -> (int, bool):
        left = 0
        right = len(nums) - 1

        while True:
            if left == right:
                if nums[left] == target:
                    return left, True
                elif nums[left]

    def searchMatrix(self, matrix: list, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # take care of the square matrix at the upper-left corner
        diagonal = [matrix[d][d] for d in range(min((m, n)))]

        diag_index, find = self.binary_search(diagonal, target)

        if find:
            return True
        else:
            # search vertically
            _, find = self.binary_search([matrix[r][diag_index] for r in range(diag_index)])

            if find:
                return True
            
            # search horizontally
            _, find = self.binary_search([matrix[diag_index][c] for c in range(diag_index)])

            if find:
                return True
        
        # take care of the rest of items

        if m > n:
            for row in matrix[n:]:
                _, find = self.binary_search(row, target)

                if find:
                    return True
        else:
            cols = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
            for col in cols:
                _, find = self.binary_search(col, target)

                if find:
                    return True

        return False