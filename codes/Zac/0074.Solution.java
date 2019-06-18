class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null
                || matrix.length == 0
                || matrix[0] == null
                || matrix[0].length == 0
                || matrix[0][0] > target) {
            return false;
        }
        int R = matrix.length, C = matrix[0].length;

        // search in rows
        int lo = 0;
        int hi = R - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (matrix[mid][0] <= target && matrix[mid][C - 1] >= target) {
                lo = mid;
                break;
            } else if (matrix[mid][0] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        R = lo;

        // search in column
        lo = 0;
        hi = C - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (matrix[R][mid] < target) {
                lo = mid + 1;
            } else if (matrix[R][mid] > target) {
                hi = mid - 1;
            } else {
                return true;
            }
        }
        return matrix[R][lo] == target;
    }
}