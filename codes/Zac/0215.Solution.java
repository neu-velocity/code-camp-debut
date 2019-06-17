class Solution {
    // Heap
    // TC: O(Nlogk)
    // SC: O(N)
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue();
        for (int n : nums) {
            minHeap.offer(n);
            while (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        return minHeap.poll();
    }
}