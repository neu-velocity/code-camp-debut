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
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (m > 1) {
            prev = prev.next;
            m--;
            n--;
        }
        head = prev.next;
        ListNode tail = prev.next, next = head.next;
        while (n > 1) {
            ListNode tmp = next.next;
            next.next = head;
            head = next;
            next = tmp;
            n--;
        }
        prev.next = head;
        tail.next = next;
        return dummy.next;
    }
}