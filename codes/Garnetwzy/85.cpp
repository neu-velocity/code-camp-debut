class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0)
            return 0;
        int n = matrix[0].size();
        vector<int> height(n, 0);
        vector<int> left(n, 0);
        vector<int> right(n, n);
        int maxVal = 0;
        for(int i = 0; i < matrix.size(); i++) {
            int curLeft = 0, curRight = n;
            for(int j = 0; j < n; j++) {
                if(matrix[i][j] == '1') {
                    height[j]++;
                    left[j] = max(left[j], curLeft);
                }else{
                    height[j] = 0;
                    left[j] = 0;
                    curLeft = j+1;
                }
            }
            for(int j = n-1; j >= 0; j--) {
                if(matrix[i][j] == '1') {
                    right[j] = min(right[j], curRight);
                }else{
                    right[j] = n;
                    curRight = j;
                }
            }
            for(int i = 0; i < n; i++) {
                maxVal = max(maxVal, height[i] * (right[i] - left[i]));
            }
        }
        return maxVal;
    }
};