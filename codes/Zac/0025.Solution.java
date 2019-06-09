/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // Stack
    // TC: O(n)
    // SC: O(k)
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k <= 1) {
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        Stack<ListNode> stack = new Stack();
        ListNode prev = dummy, next = prev.next;
        while (next != null) {
            while (next != null && stack.size() < k) {
                stack.push(next);
                next = next.next;
            }
            if (stack.size() == k) {
                // reverse
                while (!stack.isEmpty()) {
                    ListNode node = stack.pop();
                    prev.next = node;
                    prev = node;
                }
                prev.next = next;
            }
        }
        return dummy.next;
    }

    // constant space
    // TC: O(n)
    // SC: O(1)
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k <= 1) {
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy, tail = head, next = head;

        while (next != null) {
            int t = k;
            while (t > 0 && next != null) {
                next = next.next;
                t--;
            }
            if (t > 0) {
                break;
            }
            head = prev.next;
            tail = head;
            next = head.next;
            t = k;
            while (t > 1) {
                ListNode tmp = next.next;
                next.next = head;
                head = next;
                next = tmp;
                t--;
            }
            tail.next = next;
            prev.next = head;
            prev = tail;
        }
        return dummy.next;
    }
}