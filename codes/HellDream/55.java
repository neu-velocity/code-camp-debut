class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length<=1) return true;
        int max = 0;
        for(int i=0;i<nums.length&&i<=max;i++){
            if(nums[i]!=0)
                max = Math.max(max, nums[i]+i);
            if(max>=nums.length-1) return true;
        }
        return false;
    }
}