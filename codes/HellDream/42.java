class Solution {
    public int trap(int[] height) {
        int max = 0;
        int leftMax =0, rightMax = 0;
        int left = 0, right = height.length-1;
        while(left<right){
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            if(leftMax<rightMax){
                max += leftMax-height[left];
                left++;
            }else{
                max+= rightMax-height[right];
                right--;
            }
        }
        return max;
    }
}