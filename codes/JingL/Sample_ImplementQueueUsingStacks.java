package Leetcode;

import java.util.Deque;
import java.util.LinkedList;

public class _1_1_ImplementQueueUsingStacks {

    /**
     *
     * Leetcode: 232 easy
     * Date: 201902
     *
     * 解题思路：
     *  Stack后进先出，两个Stack一个用来Input，一个用来Output，是数据存储和调用顺序符合FIFO。
     *  关键在于Shuffle功能：如果input中有数据尚未处理，将其转入output中进行 查看 和 删除
     *
     *
     * 注意事项：
     * 1.peek() 与 pop() 均需调用Shuffle功能。
     * 2.注意如果queue中没有element，返回何值
     * 3.isEmpty()需查看input和output中均不存在element
     *
     *
     * */

    Deque<Integer> inStack;
    Deque<Integer> outStack;

    public _1_1_ImplementQueueUsingStacks(){

        inStack = new LinkedList<>();
        outStack = new LinkedList<>();

    }

    /* important: 如果inStack中有element而outStack中无元素，将其全部转入outStack进行查看和输出*/

    public void shuffle(){
        if(outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
    }


    public void push(int x){
        inStack.push(x);
    }

    //Attention: if the queue is empty, return -1;
    public int pop(){
        shuffle();
        if(outStack.isEmpty()){
            return -1;
        }else{
            return outStack.pop();
        }
    }

    //Attention: if the queue is empty, return -1;
    public int peek(){
        shuffle();
        if(outStack.isEmpty()){
            return -1;
        }else {
            return outStack.peek();
        }
    }

    public boolean isEmpty(){
        return inStack.isEmpty() && outStack.isEmpty();
    }


    public static void main(String[] args) {

    }

}
