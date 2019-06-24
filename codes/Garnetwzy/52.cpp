class Solution {
public:
    int totalNQueens(int n) {
        vector<bool> colomn(n, false);
        vector<bool> leftTop(2*n, false);
        vector<bool> rightTop(2*n, false);
        int count = 0;
        dfs(colomn, leftTop, rightTop, 0, count);
        return count;
    }
    
    void dfs(vector<bool>& colomn, vector<bool>& leftTop, vector<bool>& rightTop, int row, int &count) {
        if(row == colomn.size()) {
            count++;
            return;
        }
        int n = colomn.size();
        for(int i = 0; i < n; i++) { //(row, i)
            int leftTopIndex = i + row;
            int rightTopIndex = row + n - 1 - i;
            if(colomn[i] || leftTop[leftTopIndex] || rightTop[rightTopIndex]) {
                 continue;
            }
            colomn[i] = leftTop[leftTopIndex] = rightTop[rightTopIndex] = true;
            dfs(colomn, leftTop, rightTop, row+1, count);
            colomn[i] = leftTop[leftTopIndex] = rightTop[rightTopIndex] = false;
        }
    }
    
    
};