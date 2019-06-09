/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    // HashMap
    // TC: O(n)
    // SC: O(n)
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        Map<Node, Node> map = new HashMap();
        Node oldNode = head;
        while (oldNode != null) {
            Node newNode = new Node();
            newNode.val = oldNode.val;
            map.put(oldNode, newNode);
            oldNode = oldNode.next;
        }
        oldNode = head;
        while (oldNode != null) {
            Node newNode= map.get(oldNode);
            newNode.random = map.get(oldNode.random);
            if (oldNode.next != null) {
                newNode.next = map.get(oldNode.next);
            }
            oldNode = oldNode.next;
        }
        return map.get(head);
    }

    // Constant space
    // TC: O(n) - three passes
    // SC: O(1)
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        // clone
        Node curr = head;
        while (curr != null) {
            Node node = new Node();
            node.val = curr.val;
            node.next = curr.next;
            curr.next = node;
            curr = node.next;
        }
        // copy random
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        // seperate
        Node newHead = head.next;
        Node n1 = head, n2 = newHead;
        while (n1 != null) {
            n1.next = n2.next;
            n1 = n1.next;
            if (n1 != null) {
                n2.next = n1.next;
            } else {
                n2.next = null;
            }
            n2 = n2.next;
        }
        return newHead;
    }
}