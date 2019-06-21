class Solution:
    def __init__(self):
        self.matrix = [[]]
        self.target = -999

    def binary_search_2D(self, upper: int, lower: int, left: int, right: int) -> bool:
        if upper > lower or left > right:
            if self.matrix[lower][right] == self.target:
                return True
            else:
                return False

        vertical_mid = (upper + lower) // 2
        horizontal_mid = (left + right) // 2

        if self.matrix[vertical_mid][horizontal_mid] == self.target:
            return True
        else:
            if self.matrix[vertical_mid][horizontal_mid] > self.target:
                return self.binary_search_2D(upper, vertical_mid - 1, left, right) \
                    or self.binary_search_2D(vertical_mid, lower, left, horizontal_mid - 1)
            else:
                return self.binary_search_2D(vertical_mid + 1, lower, left, right) \
                    or self.binary_search_2D(upper, vertical_mid, horizontal_mid + 1, right)


    def searchMatrix(self, matrix: list, target: int) -> bool:
        if matrix == [] or matrix == [[]]:
            return False
        
        self.matrix = matrix
        self.target = target
        
        m = len(matrix)
        n = len(matrix[0])

        return self.binary_search_2D(0, m - 1, 0, n - 1)



if __name__ == "__main__":
    solu = Solution()
    t = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    solu.searchMatrix(t, 30)