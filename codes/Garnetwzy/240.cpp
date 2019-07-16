class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size() == 0 || matrix[0].size() == 0)
            return false;
        int row = 0;
        int colomn = matrix[0].size()-1;
        while(row < matrix.size() && colomn >= 0) {
            if(matrix[row][colomn] == target)
                return true;
            if(matrix[row][colomn] > target) {
                colomn--;
            }else{
                row++;
            }
        }
        return false;
    }
};