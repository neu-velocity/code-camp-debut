class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> lists = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        Arrays.sort(nums);
        generateSubsets(lists, list, nums,0);
        return lists;
    }
    
    public void generateSubsets(List<List<Integer>> lists, List<Integer> list, int[] nums,int index){
        if(!lists.contains(list))
            lists.add(list);
        for(int i=index;i<nums.length;i++){
            List<Integer> newList = new ArrayList<>(list);
            newList.add(nums[i]);
            generateSubsets(lists, newList, nums,i+1);
        }
    }
}