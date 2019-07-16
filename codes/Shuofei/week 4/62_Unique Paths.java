class Solution {
    public int uniquePaths(int m, int n) {
        // C(m + n, n) == C(m + n, m)        
        int t = Math.max(m, n);
        double res = 1;
        for (int i = m + n - 2; i >= t; i--)
            res = res * i / (m + n - 1 - i);
        return (int)res;
    }
}

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] f = new int[m + 1][n + 1];
        f[1][1] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (!((i == 1) && (j == 1)))
                    f[i][j] = f[i-1][j] + f[i][j-1];
        return f[m][n];
    }
}