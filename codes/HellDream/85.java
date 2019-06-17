class Solution {
    public int maximalRectangle(char[][] matrix) {
        if(matrix.length==0||matrix[0].length==0) return 0;
        int[] heights = new int[matrix[0].length];
        int max = 0;
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                char c = matrix[i][j];
                if(c=='0'){
                    heights[j] = 0;
                }else{
                    heights[j] = heights[j]+1;
                }
            }
            max = Math.max(max, largestRectangleArea(heights));
        }
        return max;
    }
    
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