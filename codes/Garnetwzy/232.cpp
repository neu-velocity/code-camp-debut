class MyQueue {
public:
    /** Initialize your data structure here. */
    stack<int> s;
    stack<int> help;
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        while(!s.empty()) {
            int top = s.top();
            s.pop();
            help.push(top);
        }
        s.push(x);
        while(!help.empty()) {
            int top = help.top();
            s.push(top);
            help.pop();
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int top = s.top();
        s.pop();
        return top;
    }
    
    /** Get the front element. */
    int peek() {
        return s.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */