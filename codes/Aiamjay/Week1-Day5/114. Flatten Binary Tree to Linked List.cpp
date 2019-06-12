/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// wjcnote 这里的flatten 函数最后一行 root = new_root
// wjcnote 并没有将root值给更改了，但是new_root是正确答案
#include <list>
class Solution {
public:
    // in order
    void in_order(TreeNode* head, list<int> &l) {
        if (head == NULL)
            return ;
        l.push_back(head->val);
        if (head->left != NULL) in_order(head->left, l);
        if (head->right != NULL)in_order(head->right, l);
    }

    void flatten(TreeNode* root) {
        if (root == NULL)
            return ;
        auto a = list<int>();
        in_order(root, a);
        auto new_root = new TreeNode(a.front());
        a.pop_front();
        auto temp = new_root;
        for (int e : a) {
            temp->right = new TreeNode(e);
            temp = temp->right;
        }
        root = new_root;
        print(root);
    }

    void print(TreeNode* head) {
        while (head != NULL) {
            std::cout << head->val << " ";
            std::cout << head->left << " ";
            head = head->right;
        }
        std::cout<< endl;
    }
};