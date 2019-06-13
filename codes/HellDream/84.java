class Solution {
    public int largestRectangleArea(int[] heights) {
        if(heights.length==0) return 0;
        int max = 0;
        for(int i=0;i<heights.length;i++){
            if(i == heights.length-1|| heights[i]>heights[i+1]){
                int minHeight = heights[i];
                for(int j=i;j>=0;j--){
                    minHeight = Math.min(minHeight,heights[j]);
                    int width = i-j+1;
                    max = Math.max(max, minHeight*width);
                }
            }
        }
        return max;
    }
}