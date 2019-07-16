class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int row = board.size();
        if(row == 0)
            return;
        int colomn = board[0].size();
        for(int i = 0; i < row; i++) {
            if(board[i][0] == 'O') {
                dfs(board, i, 0);
            }
            if(board[i][colomn-1] == 'O')
                dfs(board, i, colomn-1);
        }
        for(int i = 0; i < colomn; i++) {
            if(board[0][i] == 'O'){
                dfs(board, 0, i);
            }
            if(board[row-1][i] == 'O'){
                dfs(board, row-1, i);
            }
        }
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < colomn; j++) {
                if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }else if(board[i][j] == 'y') {
                    board[i][j] = 'O';
                }
            }
        }
    }
    
    void dfs(vector<vector<char>>& board, int row, int colomn) {
        if(row < 0 || row >= board.size() || colomn < 0 || colomn >= board[0].size()) {
            return;
        }
        if(board[row][colomn] != 'O')
            return;
        board[row][colomn] = 'y';
        dfs(board, row, colomn+1);
        dfs(board, row, colomn-1);
        dfs(board, row+1, colomn);
        dfs(board, row-1, colomn);
    }
};