class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList();
        if (n <= 0) {
            return ans;
        }
        char[][] board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        dfs(board, 0, n, ans);
        return ans;
    }

    private void dfs(char[][] board, int r, int n, List<List<String>> ans) {
        if (r == n) {
            List<String> list = new ArrayList();
            for (char[] row : board) {
                list.add(new String(row));
            }
            ans.add(list);
            return;
        }

        for (int c = 0; c < n; c++) {
            if (isValid(board, r, c, n)) {
                board[r][c] = 'Q';
                dfs(board, r + 1, n, ans);
                board[r][c] = '.';
            }
        }
    }

    private boolean isValid(char[][] board, int r, int c, int n) {
        // check column
        for (int i = 0; i < n; i++) {
            if (board[i][c] == 'Q') {
                return false;
            }
        }
        // check diagonals
        int[][] dir = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        for (int[] d : dir) {
            int i = r + d[0], j = c + d[1];
            while (i >= 0 && i < n && j >= 0 && j < n) {
                if (board[i][j] == 'Q') {
                    return false;
                }
                i += d[0];
                j += d[1];
            }
        }
        return true;
    }
}