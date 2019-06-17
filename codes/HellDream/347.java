class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> list = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for(int n:nums){
            map.put(n, map.getOrDefault(n,0)+1);
        }
        TreeMap<Integer, List<Integer>> treeMap = new TreeMap<>();
        for(int key: map.keySet()){
            int value = map.get(key);
            if(!treeMap.containsKey(value)){
                treeMap.put(value, new ArrayList<>());
            }
            treeMap.get(value).add(key);
            
        }
        while(list.size()<k){
            Map.Entry<Integer, List<Integer>> entry = treeMap.pollLastEntry();
            list.addAll(entry.getValue());        
        }
        return list;
        
    }
}