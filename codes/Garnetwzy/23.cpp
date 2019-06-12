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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int len = lists.size();
        return merge(lists, 0, len-1);
    }
    
    ListNode* merge(vector<ListNode*>& lists, int s, int e) {
        if(s > e) {
            return NULL;
        }
        if(s == e)
            return lists[s];
        if(s+1 == e) {
            return merge2List(lists[s], lists[e]);
        }
        int mid = s + (e - s) / 2;
        ListNode *left = merge(lists, s, mid);
        ListNode *right = merge(lists, mid+1, e);
        return merge2List(left, right);
    }
    
    ListNode *merge2List(ListNode *l1, ListNode *l2) {
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        while(l1 && l2) {
            if(l1->val < l2->val) {
                p->next = l1;
                l1 = l1->next;
            }else{
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if(l1) {
            p->next = l1;
        }
        if(l2) {
            p->next = l2;
        }
        return head->next;
    }
    
    
};