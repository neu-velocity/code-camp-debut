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
        if (headA == null || headB == null) {
            return null;
        }
        ListNode nodeA = headA, nodeB = headB;
        ListNode tailA = null, tailB = null;
        while (true) {
            if (nodeA == nodeB) {
                return nodeA;
            }
            if (nodeA.next == null) {
                if (tailA == null) {
                    tailA = nodeA;
                } else {
                    return null;
                }
                nodeA = headB;
            } else {
                nodeA = nodeA.next;
            }
            if (nodeB.next == null) {
                if (tailB == null) {
                    tailB = nodeB;
                } else {
                    return null;
                }
                nodeB = headA;
            } else {
                nodeB = nodeB.next;
            }
            if (tailA != null && tailB != null && tailA != tailB) {
                return null;
            }
        }
    }
}