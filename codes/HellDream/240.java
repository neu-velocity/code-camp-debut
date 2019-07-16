class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length==0||matrix[0].length==0) return false;
        for(int i=0;i<matrix.length;i++){
            if(search(matrix[i],target)){
                return true;
            }
        }
        return false;
    }
    
    public boolean search(int[] nums, int target){
        int left = 0, right = nums.length-1;
        while(left+1<right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target) return true;
            else if(nums[mid]<target) left = mid;
            else right = mid;
        }
        return nums[left]==target||nums[right]==target;
    }
}