class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        permutation(lists, list, used,nums,1);
        return lists;
    }
    
    public void permutation(List<List<Integer>> lists, List<Integer> list, boolean[] used ,int[] nums, int depth){
        if(list.size()==nums.length){
            lists.add(list);
            return;
        }
        if(depth>nums.length) return;
        for(int i=0;i<nums.length;i++){
            if(!used[i]) {
                List<Integer> tmp = new ArrayList<>(list);
                tmp.add(nums[i]);
                used[i] = true;
                permutation(lists, tmp, used, nums, depth+1);
                used[i] = false;
            }
        }
    }
}