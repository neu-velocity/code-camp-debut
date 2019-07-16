class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        if(row == 0)
            return false;
        int colomn = matrix[0].size();
        if(colomn == 0)
            return false;
        int s = 0, e = row-1;
        while(s < e) {
            int mid = s + (e - s ) / 2;
            if(matrix[mid][0] < target) {
                s = mid + 1;
            }else {
                e = mid;
            }
        }
        int targetRow;
        if(matrix[s][0] == target) {
            return true;
        } else if (matrix[s][0] > target) {
            if(s == 0) {
                return false;
            }else {
                targetRow = s - 1;
            }
        } else {
            targetRow = s;
        }
        s = 0;
        e = colomn-1;
        while(s <= e) {
            int mid = s + (e - s) / 2;
            if(matrix[targetRow][mid] == target)
                return true;
            if(matrix[targetRow][mid] > target) {
                e = mid - 1;
            }else {
                s = mid + 1;
            }
        }
        return false;
    }
};