class Solution {
    public List<List<String>> solveNQueens(int n){
        List<List<String>> lists = new ArrayList<>();
        List<String> list = new ArrayList<>(n);
        nQueens(n, 0, new boolean[n], new boolean[2*n-1], new boolean[2*n-1], lists, list);
        return lists;
    }

    public void nQueens(int n, int x,
                        boolean[] cols, boolean[] diag1, boolean[] diag2,
                        List<List<String>> lists, List<String> list){
        if(x==n) {
            lists.add(list);
            return;
        }
        for(int y=0;y<n;y++){
            int idx1 = x+y, idx2 = n-1-x+y;
            if(!cols[y]&&!diag1[idx1]&&!diag2[idx2]){
                char[] chars = new char[n];
                Arrays.fill(chars, '.');
                chars[y] = 'Q';
                List<String> tmp = new ArrayList<>(list);
                tmp.add(new String(chars));
                cols[y] = true; diag1[idx1] = true; diag2[idx2] = true;
                nQueens(n, x+1, cols, diag1, diag2, lists, tmp);
                cols[y] = false; diag1[idx1] = false; diag2[idx2] = false;
            }
        }
    }
}