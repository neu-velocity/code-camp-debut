/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        ListNode p1 = headA, p2 = headB;
        if(lenA>lenB){
            for(int i=0;i<lenA-lenB;i++){
                p1 = p1.next;
            }
        }else{
            for(int i=0;i<lenB-lenA;i++){
                p2 = p2.next;
            }
        }
        while(p1!=null&&p2!=null){
            if(p1==p2) return p1;
            p1 = p1.next;
            p2 = p2.next;
        }
        return null;
    }

    public int getLength(ListNode node){
        int len = 0;
        while(node!=null){
            node  =node.next;
            len++;
        }
        return len;
    }
}