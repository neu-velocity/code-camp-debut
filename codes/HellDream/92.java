/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if(head==null||head.next==null||m==n) return head;
        ListNode curr = head;
        ListNode beforeCurr = null;
        for(int i=0;i<m-1;i++){
            beforeCurr = curr;
            curr = curr.next;
        }
        ListNode prev = head;
        for(int i=0;i<n;i++){
            prev = prev.next;
        }
        for(int i=0;i<n-m+1;i++){
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        if(beforeCurr!=null){
            beforeCurr.next = prev;
            return head;                
        }
        return prev;
    }
}