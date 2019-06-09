/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *p = NULL;
        ListNode *current = p;
        while(head) {
            ListNode *tmp = head->next;
            head->next = p;
            p = head;
            head = tmp;
        }
        return p;
        
    }
};