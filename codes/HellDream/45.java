class Solution {
    public int jump(int[] nums) {
        if(nums.length<=1) return 0;
        int steps = 0, currentMax = 0, farthest = 0;
        for(int i=0;i<nums.length;i++){
            farthest = Math.max(farthest, nums[i]+i);
            if(i == currentMax){
                currentMax = farthest;
                steps++;
                if(farthest>=nums.length-1) break;
            }
            
        }
        return steps;
    }
}