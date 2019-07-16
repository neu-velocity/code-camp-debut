class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1, -1);
        dp[0] = 1;
        return help(nums, dp, target);
    }
    
    int help(vector<int>& nums, vector<int>& dp, int target) {
        if(dp[target] != -1)
            return dp[target];
        int ret = 0;
        for(int num: nums) {
            if(num <= target) {
                ret += help(nums, dp, target-num);
            }
        }
        dp[target] = ret;
        return ret;
    }
    
};