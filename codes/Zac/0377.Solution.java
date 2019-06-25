class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        for (int i = 1; i <= target; i++) {
            for (int n : nums) {
                if (i > n) {
                    dp[i] += dp[i - n];
                } else if (i == n) {
                    dp[i] += 1;
                }
            }
        }
        return dp[target];
    }
}