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
    ListNode* sortList(ListNode* head) {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *p = head;
        int size = 0;
        while(p) {
            size++;
            p = p->next;
        }
        ListNode *first = head;
        ListNode *second = dummy;
        ListNode *cur;
        ListNode *pre;
        for(int len = 1; len <= size; len = len * 2) {
            cur = dummy->next;
            pre = dummy;
            while(cur) {
                first = cur;
                second = breakNode(first, len);
                cur = breakNode(second, len);
                pre = merge(first, second, pre);
            }
        }
        return dummy->next;
    }
    
    ListNode *breakNode(ListNode *head, int len) {
        for(int i = 1; head && i < len; i++) {
            head = head->next;
        }
        if(head == NULL)
            return NULL;
        ListNode *second = head->next;
        head->next = NULL;
        return second;
    }
    
    ListNode* merge(ListNode *first, ListNode *second, ListNode *pre) {
        ListNode *p1 = first;
        ListNode *p2 = second;
        ListNode *tmp;
        while(p1 && p2) {
            if(p1->val < p2->val) {
                pre->next = p1;
                tmp = p1->next;
                p1->next = NULL;
                p1 = tmp;
            } else {
                pre->next = p2;
                tmp = p2->next;
                p2->next = NULL;
                p2 = tmp;
            }
            pre = pre->next;
        }
        if(p1) {
            pre->next = p1;
        }
        if(p2) {
            pre->next = p2;
        }
        while(pre->next) {
            pre = pre->next;
        }
        return pre;
            
    }
};