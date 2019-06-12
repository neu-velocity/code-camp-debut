class MyStack {
    private Queue<Integer> q1;
    private Queue<Integer> q2;

    public MyStack() {
        q1 = new ArrayDeque<>();
        q2 = new ArrayDeque<>();
    }
    /** Push element x onto stack. */
    public void push(int x) {
        if(q1.isEmpty()){
            q1.offer(x);
        }else{
            while(!q1.isEmpty()){
                int i = q1.poll();
                q2.offer(i);
            }
            q1.offer(x);
            while(!q2.isEmpty()){
                int i = q2.poll();
                q1.offer(i);
            }
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return q1.poll();
    }

    /** Get the top element. */
    public int top() {
        return q1.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty() &&q2.isEmpty();
    }
}
