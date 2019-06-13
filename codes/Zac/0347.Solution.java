class Solution {
    // Heap
    // TC: O(N + Nlogk) = O(Nlogk)
    // SC: O(N)
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap();
        for (int n : nums) {
            countMap.put(n, countMap.getOrDefault(n, 0) + 1);
        }
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>((o1, o2) -> countMap.get(o1) - countMap.get(o2));
        for (int n : countMap.keySet()) {
            minHeap.offer(n);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return new ArrayList(minHeap);
    }
}