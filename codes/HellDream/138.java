class Solution {
    public Node copyRandomList(Node head) {
        if(head==null) return null;
        Node dummy = new Node(0,null,null);
        Node curr = dummy;
        HashMap<Node, Node> map = new HashMap<>();
        while(head!=null){
            if(!map.containsKey(head)){
                map.put(head, new Node(head.val, null, null));
            }
            curr.next = map.get(head);
            if(head.random!=null){
                if(!map.containsKey(head.random)){
                    map.put(head.random, new Node(head.random.val, null, null));
                }
            }
            curr.next.random = map.get(head.random);
            head = head.next;
            curr = curr.next;
        }
        return dummy.next;
    }
}