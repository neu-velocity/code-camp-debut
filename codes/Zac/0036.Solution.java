class Solution {
    public boolean isValidSudoku(char[][] board) {
        int N = 9;
        boolean[] seen = new boolean[9];
        // check rows
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (board[r][c] != '.') {
                    if (seen[board[r][c] - '1']) {
                        return false;
                    } else {
                        seen[board[r][c] - '1'] = true;
                    }
                }
            }
            Arrays.fill(seen, false);
        }
        // check column
        for (int c = 0; c < N; c++) {
            for (int r = 0; r < N; r++) {
                if (board[r][c] != '.') {
                    if (seen[board[r][c] - '1']) {
                        return false;
                    } else {
                        seen[board[r][c] - '1'] = true;
                    }
                }
            }
            Arrays.fill(seen, false);
        }
        // check sub-boxes
        for (int x = 1; x < N; x += 3) {
            for (int y = 1; y < N; y += 3) {
                for (int r = x - 1; r <= x + 1; r++) {
                    for (int c = y - 1; c <= y + 1; c++) {
                        if (board[r][c] != '.') {
                            if (seen[board[r][c] - '1']) {
                                return false;
                            } else {
                                seen[board[r][c] - '1'] = true;
                            }
                        }
                    }
                }
                Arrays.fill(seen, false);
            }
        }
        return true;
    }
}