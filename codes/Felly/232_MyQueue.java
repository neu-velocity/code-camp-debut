class MyQueue {

    private Stack<Integer> origin = new Stack<>();
    private Stack<Integer> adverse = new Stack<>();
    
    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        Integer Int = new Integer(x);
        origin.push(Int);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        reserving(origin, adverse);
        int result = adverse.pop();
        reserving(adverse, origin);
        return result;
    }
    
    /** Get the front element. */
    public int peek() {
        reserving(origin, adverse);
        int result = adverse.peek();
        reserving(adverse, origin);
        return result;
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return origin.isEmpty() && adverse.isEmpty();
    }
    
    private void reserving(Stack<Integer> A, Stack<Integer> B) {
        if (B.isEmpty()) {
            while (!A.isEmpty()) {
                B.push(A.pop());
            }
        }
    }
    
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */