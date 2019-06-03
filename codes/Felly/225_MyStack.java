class MyStack {

    private Queue<Integer> queue = new LinkedList<>();
    
    /** Initialize your data structure here. */
    public MyStack() {
        
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue.offer(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int length = queue.size();
        while (length != 1) {
            queue.offer(queue.poll());
            length--;
        }
        return queue.poll();
    }
    
    /** Get the top element. */
    public int top() {
        int length = queue.size();
        while (length != 1) {
            queue.offer(queue.poll());
            length--;
        }
        int result = queue.poll();
        queue.offer(result);
        return result;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue.isEmpty();
    }
    
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */