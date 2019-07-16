class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }
    
    public boolean solve(char[][] board){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]=='.'){
                    for(char c='1';c<='9';c++){
                        if(isValid(board, i,j, c)){
                            board[i][j] = c;
                            if(solve(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    
    private boolean isValid(char[][] board, int row, int col, char value){
        for(int i=0;i<9;i++){
            if(board[row][i]!='.'&&board[row][i]==value) return false;
            if(board[i][col]!='.'&&board[i][col]==value) return false;
            if(board[3 * (row / 3) + i / 3][3*(col/3)+i%3]!='.' && 
               board[3 * (row / 3) + i / 3][3*(col/3)+i%3]==value) return false;
        }
        return true;
    }
}