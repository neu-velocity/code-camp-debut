class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        combination(lists, list, candidates, target, 0, 0);
        return lists;
    }
    
    public void combination(List<List<Integer>> lists,List<Integer> list,int[] candidates, int target, int sum, int start){
        if(sum > target){
            return;
        }
        if(sum==target){
            lists.add(list);
            return;
        }
        for(int i=start;i<candidates.length;i++){
            if(sum+candidates[i]<=target){
                List<Integer> tmplist = new ArrayList<>(list);
                tmplist.add(candidates[i]);
                combination(lists, tmplist, candidates, target, sum+candidates[i],i);
            }
        }
    }
}