/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head)
            return head;
        Node *newHead = new Node(0, NULL, NULL);
        Node *current = newHead;
        Node* p = head;
        map<Node *, Node *> hash;
        hash[p] = current;
        while(p) {
            current->val = p->val;
            if(p->next) {
               if(hash.find(p->next) != hash.end()) {
                    current->next = hash[p->next];            
                }else {
                    hash[p->next] = new Node(0, NULL, NULL);   
                    current->next = hash[p->next];
                } 
            }
            
            if(p->random) {
                if(hash.find(p->random) != hash.end()) {
                    current->random = hash[p->random];
                }else{
                    hash[p->random] = new Node(0, NULL, NULL);
                    current->random = hash[p->random];
                }
            }
            p = p->next;
            current = current->next;
        }
        return newHead;
    }
};