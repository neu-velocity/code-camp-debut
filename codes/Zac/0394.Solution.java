class MyStack {

    private Queue<Integer> q1, q2;

    /** Initialize your data structure here. */
    public MyStack() {
        this.q1 = new LinkedList();
        this.q2 = new LinkedList();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        while (!q2.isEmpty()) {
            q1.offer(q2.poll());
        }
        q1.offer(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        if (q2.isEmpty()) {
            transfer();
        }
        return q2.poll();
    }

    /** Get the top element. */
    public int top() {
        if (q2.isEmpty()) {
            transfer();
        }
        return q2.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }

    private void transfer() {
        q2 = q1;
        q1 = new LinkedList();
        while (q2.size() > 1) {
            q1.offer(q2.poll());
        }
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