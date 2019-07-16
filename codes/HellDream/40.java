class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list  =new ArrayList<>();
        boolean[] isUsed = new boolean[candidates.length];
        combination(lists, list, candidates, target, 0, 0);
        return lists;
    }
    
    public void combination(List<List<Integer>> lists, List<Integer> list,int[] candidates,
                             int target, int sum, int start){
        if(sum==target){
            lists.add(list);
            return;
        }

        for(int i=start;i<candidates.length;i++){
            if(sum+candidates[i]>target) break;
            List<Integer> tmp = new ArrayList<>(list);
            tmp.add(candidates[i]);
            combination(lists, tmp, candidates, target, sum+candidates[i], i+1);
            while(i+1<candidates.length&&candidates[i]==candidates[i+1]) i++;
        }
    }
}