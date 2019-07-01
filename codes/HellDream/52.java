class Solution {
    private int res = 0;
    public int totalNQueens(int n) {
        nQueens(n, 0, new boolean[n], new boolean[2*n-1], new boolean[2*n-1]);
        return res;
    }
    
    public void nQueens(int n, int x,
                        boolean[] cols, boolean[] diag1, boolean[] diag2){
        if(x==n) {
            res++;
            return;
        }
        for(int y=0;y<n;y++){
            int idx1 = x+y, idx2 = n-1-x+y;
            if(!cols[y]&&!diag1[idx1]&&!diag2[idx2]){
                cols[y] = true; diag1[idx1] = true; diag2[idx2] = true;
                nQueens(n, x+1, cols, diag1, diag2);
                cols[y] = false; diag1[idx1] = false; diag2[idx2] = false;
            }
        }
    }
}