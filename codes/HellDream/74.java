class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        if(matrix==null||rows==0) return false;
        int cols = matrix[0].length;
        if(cols==0) return false;
        int start = 0, end = rows-1;
        while(start+1<end){
            int mid = start+(end-start)/2;
            if(matrix[mid][0]==target) return true;
            if(matrix[mid][0]<target){
                start = mid;
            }else{
                end = mid;
            }
        }
        int left = 0, right = cols-1;
        int beginRow = start;
        if(matrix[end][0]<=target){
            beginRow = end;
        }
        while(left+1<right){
            int mid = left+(right-left)/2;
            if(matrix[beginRow][mid]==target) return true;
            if(matrix[beginRow][mid]<target){
                left = mid;
            }else{
                right = mid;
            }
        }
        if(matrix[beginRow][left]==target) return true;
        if(matrix[beginRow][right]==target) return true;
        
        return false;
    }
}