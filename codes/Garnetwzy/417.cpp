class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        int row = matrix.size();
        vector<vector<int>> ret;
        if(row == 0)
            return ret;
        int colomn = matrix[0].size();
        vector<vector<bool>> visit1(row, vector<bool>(colomn, false));
        vector<vector<bool>> visit2(row, vector<bool>(colomn, false));
        vector<vector<int>> directs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        getTopLeft(visit1, matrix, row, colomn, directs);
        getBottomRight(visit2, matrix, row, colomn, directs);
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < colomn; j++) {
                if(visit1[i][j] && visit2[i][j]){
                    vector<int> tmp = {i, j};
                    ret.push_back(tmp);
                }
            }
        }
        return ret;
    }

   void getBottomRight(vector<vector<bool>>& visit, vector<vector<int>>& matrix, int row, int colomn, vector<vector<int>>& directs) {
        queue<vector<int>> q;
        for(int i = 0; i < row; i++) {
            visit[i][colomn-1] = true;
            q.push({i, colomn-1});
        }
        for(int i = 0; i < colomn-1; i++) {
            visit[row-1][i] = true;
            q.push({row-1, i});
        }
        while(!q.empty()) {
            vector<int> point = q.front();
            q.pop();
            int pointRow = point[0];
            int pointColomn = point[1];
            for(vector<int> direct: directs) {
                int newRow = pointRow + direct[0];
                int newColomn = pointColomn + direct[1];
                if(newRow < 0 || newRow >= row || newColomn < 0 || newColomn >= colomn) {
                    continue;
                }
                if(visit[newRow][newColomn])
                    continue;
                if(matrix[newRow][newColomn] >= matrix[pointRow][pointColomn]) {
                    visit[newRow][newColomn] = true;
                    q.push({newRow, newColomn});
                }
            }
        }
     }

       void getTopLeft(vector<vector<bool>>& visit, vector<vector<int>>& matrix, int row, int colomn, vector<vector<int>>& directs) {
        queue<vector<int>> q;
        for(int i = 0; i < colomn; i++) {
            visit[0][i] = true;
            q.push({0, i});
        }
        for(int i = 1; i < row; i++) {
            visit[i][0] = true;
            q.push({i, 0});
        }
        while(!q.empty()) {
            vector<int> point = q.front();
            q.pop();
            int pointRow = point[0];
            int pointColomn = point[1];
            for(vector<int> direct: directs) {
                int newRow = pointRow + direct[0];
                int newColomn = pointColomn + direct[1];
                if(newRow < 0 || newRow >= row || newColomn < 0 || newColomn >= colomn) {
                    continue;
                }
                if(visit[newRow][newColomn])
                    continue;
                if(matrix[newRow][newColomn] >= matrix[pointRow][pointColomn]) {
                    visit[newRow][newColomn] = true;
                    q.push({newRow, newColomn});
                }
            }
        }
     }
};