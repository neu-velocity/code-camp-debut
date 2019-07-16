class Solution {
    // TC: O(m+n)
    // SC: O(1)
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null
                || matrix.length == 0
                || matrix[0] == null
                || matrix[0].length == 0
                || matrix[0][0] > target) {
            return false;
        }
        int R = matrix.length, C = matrix[0].length;
        int r = R - 1, c = 0;
        while (r >= 0 && c < C) {
            if (matrix[r][c] > target) {
                r--;
            } else if (matrix[r][c] < target) {
                c++;
            } else {
                return true;
            }
        }
        return false;
    }
}