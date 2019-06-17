/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // Heap
    // TC: O(NlogM) - which N is the total number of nodes, M is the length of lists
    // SC: O(M) - the heap size can grows up to lists.length at most
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode(0);

        // init heap
        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>((o1, o2) -> o1.val - o2.val);
        for (ListNode n : lists) {
            if (n != null) {
                queue.offer(n);
            }
        }

        ListNode cur = dummy;
        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            cur.next = node;
            if (node.next != null) {
                queue.offer(node.next);
            }
            cur = cur.next;
        }

        return dummy.next;
    }
}