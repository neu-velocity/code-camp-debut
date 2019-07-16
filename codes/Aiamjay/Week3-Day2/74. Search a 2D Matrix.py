# encoding=utf-8


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        def column_binary_search(begin, end):
            if begin == end:
                return begin if target >= matrix[begin][0] else begin - 1
            mid = (begin + end) // 2
            if target > matrix[mid][0]:
                return column_binary_search(min(mid + 1, end), end)
            else:
                return column_binary_search(begin, mid)

        def row_binary_search(begin, end):
            if begin == end:
                return True if target == matrix[target_row][begin] else False
            mid = (begin + end) // 2
            if target > matrix[target_row][mid]:
                return row_binary_search(min(mid + 1, end), end)
            else:
                return row_binary_search(begin, mid)

        if not matrix:
            return False
        row_len = len(matrix[0])
        if not row_len:
            return False
        column_len = len(matrix)
        target_row = column_binary_search(min(1, column_len - 1), column_len - 1)
        return row_binary_search(0, row_len - 1)

    def test_solution(self):
        # case1
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        assert self.searchMatrix(matrix, target) is True

        # case2
        target = 13
        assert self.searchMatrix(matrix, target) is False

        # case3
        target = -1
        assert self.searchMatrix(matrix, target) is False

        # my case4
        matrix = [
            []
        ]
        target = 0
        assert self.searchMatrix(matrix, target) is False

        # my case5
        matrix = [
        ]
        target = 0
        assert self.searchMatrix(matrix, target) is False

        # my case6
        matrix = [
            [1, 2, 3]
        ]
        target = 3
        assert self.searchMatrix(matrix, target) is True

    def test_wrong_case(self):
        matrix = [
            [1]
        ]
        target = 0
        assert self.searchMatrix(matrix, target) is False


if __name__ == '__main__':
    s = Solution()
    s.test_solution()
    s.test_wrong_case()
