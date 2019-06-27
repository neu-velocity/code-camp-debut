class Solution {
    // dp
    // TC: O(n^n)
    // SC: O(n)
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        dp[0] = true;
        for (int i = 0; i < nums.length; i++) {
            if (dp[i]) {
                for (int j = i + 1; j < nums.length && j <= i + nums[i]; j++) {
                    dp[j] = true;
                }
            }
        }
        return dp[dp.length - 1];
    }

    // greedy
    // TC: O(n)
    // SC: O(1)
    public boolean canJump(int[] nums) {
        int pos = nums.length - 1;
        for (int i = pos - 1; i >= 0; i--) {
            if (i + nums[i] >= pos) {
                pos = i;
            }
        }
        return pos == 0;
    }
}