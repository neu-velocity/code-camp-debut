class Solution {
    int N, ans;
    boolean[] cols, digL, digR;
    public int totalNQueens(int n) {
        if (n <= 0) {
            return 0;
        }
        ans = 0;
        N = n;
        cols = new boolean[N];
        digL = new boolean[N * 2 - 1];
        digR = new boolean[N * 2 - 1];
        dfs(0);
        return ans;
    }

    private void dfs(int r) {
        if (r == N) {
            ans++;
        }
        for (int c = 0; c < N; c++) {
            if (!cols[c] && !digL[r - c + N - 1] && !digR[r + c]) {
                cols[c] = digL[r - c + N - 1] = digR[r + c] = true;
                dfs(r + 1);
                cols[c] = digL[r - c + N - 1] = digR[r + c] = false;
            }
        }
    }
}