class Solution {
    public boolean search(int[] nums, int target) {
        if(nums==null||nums.length==0) return false;
        int left=0,right=nums.length-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target) return true;
            if(nums[left]==nums[mid]){
                left++;
            }
            else if(nums[mid]<nums[left]){
                if(target>nums[mid]&&target<=nums[right])
                    left = mid;
                else right = mid-1;
            }
            else{
                if(target<nums[mid]&&target>=nums[left])
                    right = mid;
                else left = mid+1;
            }
        }
        return false;
    }
}