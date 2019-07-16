class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        combination(lists, list, k,n, 1);
        return lists;
    }
    
    public void combination(List<List<Integer>> lists, List<Integer> list, int k, int n, int start){
        if(list.size()==k&&n==0){
            lists.add(list);
            return;
        }
        if(n<0){
            return;
        }
        for(int i=start;i<=9;i++){
            List<Integer> tmp = new ArrayList<>(list);
            tmp.add(i);
            combination(lists, tmp, k, n-i, i+1);
        }
    }
}