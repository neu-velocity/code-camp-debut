/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while(prev!=null){
            prev = reverse(prev, k);
        }
        return dummy.next;
    }
    public ListNode reverse(ListNode prev, int k){
        ListNode last = prev;
        for(int i=0;i<=k;i++){
            last = last.next;
            if(i!=k && last == null) return null;
        }
        ListNode tail = prev.next;
        ListNode curr = prev.next.next;
        while(curr!=last){
            ListNode tmp = curr.next;
            curr.next = prev.next;
            prev.next = curr;
            tail.next = tmp;
            curr = tmp;
        }
        return tail;
    }
}