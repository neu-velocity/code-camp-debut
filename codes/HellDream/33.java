class Solution {
    public int search(int[] nums, int target) {
        if(nums.length==0) return -1;
        int left = 0, right = nums.length-1;
        while(left+1<right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]<nums[left]){
                if(target>nums[mid]&&target<=nums[right]){
                    left = mid+1;
                }else right = mid-1;
            }else{
                if(target<nums[mid]&& target>=nums[left]){
                    right = mid-1;
                }else left = mid+1;
            }
        }
        if(nums[left]==target)return left;
        if(nums[right]==target) return right;
        return -1;
    }
}