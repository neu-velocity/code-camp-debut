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
    bool isPalindrome(ListNode* head) {
        ListNode* first = head;
        ListNode* second = head;
        while(second && second->next) {
            first = first->next;
            second = second->next->next;
        }
        ListNode *head2 = reverse(first);
        while(head2) {
            if(head->val != head2->val)
                return false;
            head = head->next;
            head2 = head2->next;
        } 
        return true;
    }
    
    ListNode* reverse(ListNode *head) {
        ListNode *pre = NULL;
        while(head) {
            ListNode*tmp = head->next;
            head->next = pre;
            pre = head;
            head = tmp;
        }
        return pre;
    }
    
};