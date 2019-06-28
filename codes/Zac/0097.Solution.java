class Solution {
    // bottom-up
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
        dp[0][0] = true;
        for (int i = 1; i <= s2.length(); i++) {
            if (s3.charAt(i - 1) == s2.charAt(i - 1)) {
                dp[0][i] = true;
            } else {
                break;
            }
        }
        for (int i = 1; i <= s1.length(); i++) {
            dp[i][0] = dp[i - 1][0] && s3.charAt(i - 1) == s1.charAt(i - 1);
            for (int j = 1; j <= s2.length(); j++) {
                dp[i][j] = (s3.charAt(i + j - 1) == s1.charAt(i - 1) && dp[i - 1][j])
                        || (s3.charAt(i + j - 1) == s2.charAt(j - 1) && dp[i][j - 1]);
            }
        }
        return dp[s1.length()][s2.length()];
    }

    // top-down with memo
    private Map<String, Boolean> cache = new HashMap();
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length()) {
            return false;
        }
        if (s3.length() == 0) {
            return true;
        }
        if (s1.length() == 0) {
            return s2.equals(s3);
        }
        if (s2.length() == 0) {
            return s1.equals(s3);
        }
        String key = s1.length() + "/" + s2.length();
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        boolean res = (s1.charAt(0) == s3.charAt(0) && isInterleave(s1.substring(1), s2, s3.substring(1)))
                || (s2.charAt(0) == s3.charAt(0) && isInterleave(s1, s2.substring(1), s3.substring(1)));
        cache.put(key, res);
        return res;
    }
}