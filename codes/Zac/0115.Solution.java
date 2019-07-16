class Solution {
    public int numDistinct(String s, String t) {
        int[][] dp = new int[t.length()][s.length() + 1];
        for (int i = 1; i <= s.length(); i++) {
            dp[0][i] = dp[0][i - 1];
            if (t.charAt(0) == s.charAt(i - 1)) {
                dp[0][i] += 1;
            }
        }
        for (int i = 1; i < t.length(); i++) {
            for (int j = 1; j <= s.length(); j++) {
                if (j < i) {
                    dp[i][j] = 0;
                }
                dp[i][j] = dp[i][j - 1];
                if (t.charAt(i) == s.charAt(j - 1)) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }
        return dp[t.length() - 1][s.length()];
    }
}