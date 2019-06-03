class MyStack {

    /** Initialize your data structure here. */
    Queue<Integer> q1 = new LinkedList<Integer> ();
    Queue<Integer> q2 = new LinkedList<Integer> ();
    
    public MyStack() {
        
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        q1.add(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int temp = 0;
        int size = q1.size();
        while (size > 1){
            temp = q1.remove();
            q2.add(temp);
            size --;
        }
        temp = q1.remove();
        
        while (!q2.isEmpty()){    
            q1.add(q2.remove());
        }    
        return temp;
        
    }
    
    /** Get the top element. */
    public int top() {
        
        int temp = 0;
        while (!q1.isEmpty()){
            temp = q1.remove();
            q2.add(temp);
        }
       
        while (!q2.isEmpty()){    
            q1.add(q2.remove());
        }    
        return temp;
        
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty();
        
    }
}