class MyQueue {
    
    Stack <Integer> s1 = new Stack<>();
    Stack <Integer> s2 = new Stack<>();  
    
    /** Initialize your data structure here. */
    public MyQueue() {
        
    //Stack <Integer> s1 = new Stack<>();
    //Stack <Integer> stackTwo = new Stack<>();        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        s1.push(x);
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int size=0;
        while(!s1.empty()){
            //int y = s1.pop();
            //System.out.println(y);
            s2.push(s1.pop());
            size++;
        // System.out.println(size);
        }
        
        int temp = s2.pop();
        //System.out.println(temp);
        while(!s2.empty()){
            s1.push(s2.pop());
            }
        
         return temp;
    }
    
    /** Get the front element. */
    public int peek() {
        return s1.get(0);
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.empty();
        
    }
}