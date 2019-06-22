class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        permutation(lists, tmp, new boolean[nums.length], nums);
        return lists;
    }
        public void permutation(List<List<Integer>> lists,List<Integer> tmp, boolean[] used, int[] nums){
        if(tmp.size()==nums.length){
            lists.add(tmp);
            return;
        }
        for(int i=0;i<nums.length;i++){
            if(used[i]||(i>0&&nums[i]==nums[i-1]&&!used[i-1])){
                continue;
            }else{
                List<Integer> list = new ArrayList<>(tmp);
                list.add(nums[i]);
                used[i] = true;
                permutation(lists, list, used, nums);
                used[i] = false;
            }
        }
    }
}