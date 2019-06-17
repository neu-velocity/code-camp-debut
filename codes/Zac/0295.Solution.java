class MedianFinder {

    PriorityQueue<Integer> minHeap, maxHeap;

    /** initialize your data structure here. */
    public MedianFinder() {
        this.minHeap = new PriorityQueue();
        this.maxHeap = new PriorityQueue(Collections.reverseOrder());
    }

    public void addNum(int num) {
        if (minHeap.isEmpty() || num >= minHeap.peek()) {
            minHeap.offer(num);
        } else {
            maxHeap.offer(num);
        }
    }

    public double findMedian() {
        while (!maxHeap.isEmpty() && minHeap.size() < maxHeap.size()) {
            minHeap.offer(maxHeap.poll());
        }
        while (!minHeap.isEmpty() && maxHeap.size() + 1 < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
        if (minHeap.size() > maxHeap.size()) {
            return minHeap.peek() * 1.0;
        } else {
            return (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
    }
}