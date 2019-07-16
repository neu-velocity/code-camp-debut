class Solution {

    int N = 9;
    boolean[][] rows = new boolean[N][N];
    boolean[][] cols = new boolean[N][N];
    boolean[][][] boxes = new boolean[N][N][N];

    public void solveSudoku(char[][] board) {
        // init
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] != '.') {
                    int n = board[r][c] - '1';
                    rows[r][n] = cols[c][n] = boxes[r / 3][c / 3][n] = true;
                }
            }
        }
        dfs(board, 0);
    }

    private boolean dfs(char[][] board, int pos) {
        if (pos == N * N) {
            return true;
        }
        int r = pos / N, c = pos % N;
        if (board[r][c] == '.') {
            for (int i = 0; i < N; i++) {
                if (!rows[r][i] && !cols[c][i] && !boxes[r / 3][c / 3][i]) {
                    rows[r][i] = cols[c][i] = boxes[r / 3][c / 3][i] = true;
                    board[r][c] = (char)(i + '1');
                    if (dfs(board, pos + 1)) {
                        return true;
                    }
                    board[r][c] = '.';
                    rows[r][i] = cols[c][i] = boxes[r / 3][c / 3][i] = false;
                }
            }
            return false;
        } else {
            return dfs(board, pos + 1);
        }
    }
}