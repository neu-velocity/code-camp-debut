class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
    
    bool solve(vector<vector<char>>& board) {
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.')
                    continue;
                for(int k = '1'; k <= '9'; k++) {
                    board[i][j] = k;
                    if(isValid(board, i, j) && solve(board)) {
                        return true;
                    }
                }
                board[i][j] = '.';
                return false;
            }
        }
        return true;
    }
    
    bool isValid(vector<vector<char>>& board, int row, int colomn) {
        char target = board[row][colomn];
        for(int i = 0; i < board.size(); i++) {
            if(i == row)
                continue;
            if(board[i][colomn] == target)
                return false;
        }
        for(int i = 0; i < board.size(); i++) {
            if(i == colomn)
                continue;
            if(board[row][i] == target)
                return false;
        }
        int startRow = row / 3 * 3;
        int startColomn = colomn / 3 * 3;
        for(int i = startRow; i < startRow+3; i++) {
            for(int j = startColomn; j < startColomn+3; j++) {
                if(i == row && j == colomn)
                    continue;
                if(board[i][j] == target)
                    return false;
            }
        }
        return true;
    }
};