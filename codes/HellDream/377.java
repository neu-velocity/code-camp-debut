class Solution {
    public int combinationSum4(int[] nums, int target) {
        if(nums.length==0||target<0) return 0;
        int[] targets = new int[target+1];
        targets[0] = 1;
        for(int i=1;i<=target;i++){
            for(int j=0;j<nums.length;j++){
                if(i>=nums[j]){
                    targets[i] += targets[i-nums[j]];
                }
            }
        }
        return targets[target];
    }
}