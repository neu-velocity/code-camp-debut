class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        Arrays.sort(nums);
        generateSubsets(lists, list, 0,nums);
        return lists;
    }
    
    public void generateSubsets(List<List<Integer>> lists, List<Integer> list, int start, int[]nums){
        if(!lists.contains(list))
            lists.add(list);
        if(start==nums.length) return;
        for(int i=start;i<nums.length;i++){
            List<Integer> tmp = new ArrayList<>(list);
            tmp.add(nums[i]);
            generateSubsets(lists,tmp,i+1,nums);
        }
    }
}