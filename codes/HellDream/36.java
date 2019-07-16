class Solution {
    public boolean isValidSudoku(char[][] board){
        HashSet<Integer>[] rows = new HashSet[9];
        HashSet<Integer>[] cols = new HashSet[9];
        HashSet<Integer>[] blocks = new HashSet[9];
        for(int i=0;i<9;i++){
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            blocks[i] = new HashSet<>();
        }

        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[i].length;j++){
                char c = board[i][j];
                if(c!='.'){
                    int num = c-'0';
                    int idx = (i/3)*3+j/3;
                    if(rows[i].contains(num)||cols[j].contains(num)||blocks[idx].contains(num)){
                        return false;
                    }
                    rows[i].add(num);
                    cols[j].add(num);
                    blocks[idx].add(num);
                }
            }
        }
        return true;
    }
}