class Cell {
public:
    int row;
    int colomn;
    int height;
    Cell(int r,int c,int h) {
        row = r;
        colomn = c;
        height = h;
    }
};

class cmp {
public:
    bool operator()(Cell a, Cell b)
    {
        return a.height > b.height;
    }
};

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int sum = 0;
        int row = heightMap.size();
        if(row == 0)
            return sum;
        int colomn = heightMap[0].size();
        priority_queue<Cell, vector<Cell>, cmp> pq;     
        vector<vector<int>> directs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<bool>> visit(row, vector<bool>(colomn, false));
        for(int i = 0; i < row; i++) {
            pq.push(Cell(i, 0, heightMap[i][0]));
            pq.push(Cell(i, colomn-1, heightMap[i][colomn-1]));
            visit[i][0] = true;
            visit[i][colomn-1] = true;
        }
        for(int i = 0; i < colomn; i++) {
            pq.push(Cell(0, i, heightMap[0][i]));
            pq.push(Cell(row-1, i, heightMap[row-1][i]));
            visit[0][i] = true;
            visit[row-1][i] = true;
        }
        while(!pq.empty()) {
            Cell top = pq.top();
            pq.pop();
            for(vector<int> direct: directs) {
                int cellRow = top.row + direct[0];
                int cellColomn = top.colomn + direct[1];
                if(cellRow >= 0 && cellRow < row && cellColomn >= 0 && cellColomn < colomn && !visit[cellRow][cellColomn]) {
                    sum += max(0, top.height - heightMap[cellRow][cellColomn]);
                    pq.push(Cell(cellRow, cellColomn, max(heightMap[cellRow][cellColomn], top.height)));
                    visit[cellRow][cellColomn] = true;
                }
            }
        }
        return sum;
    }
    
   
};