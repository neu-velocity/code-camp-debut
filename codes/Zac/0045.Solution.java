class Solution {
    // dp
    // TC: O(n^2)
    // SC: O(n)
    public int jump(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length && j <= i + nums[i]; j++) {
                dp[j] = Math.min(dp[j], dp[i] + 1);
            }
        }
        return dp[nums.length - 1];
    }

    // dp
    // TC: O(n) - every element will be visited at most twice
    // SC: O(n)
    public int jump(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return 0;
        }
        int[] dp = new int[nums.length];
        for (int i = 0; i < dp.length; i++) {
            if (i + nums[i] >= nums.length - 1) {
                return dp[i] + 1;
            } else {
                for (int j = i + nums[i]; dp[j] == 0 && j > i; j--) {
                    dp[j] = dp[i] + 1;
                }
            }
        }
        return dp[nums.length - 1];
    }
}