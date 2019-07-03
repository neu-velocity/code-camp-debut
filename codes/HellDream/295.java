class MedianFinder {

    /** initialize your data structure here. */
    PriorityQueue<Integer> max  = new PriorityQueue<>();
    PriorityQueue<Integer> min = new PriorityQueue<>(Collections.reverseOrder());
    boolean even = true;
    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        if(even){
            max.offer(num);
            min.offer(max.poll());
        }else {
            min.offer(num);
            max.offer(min.poll());
        }
        even = !even;
    }
    
    public double findMedian() {
        if(even){
            return (max.peek()+min.peek())/2.0;
        }
        return min.peek();
    }
}