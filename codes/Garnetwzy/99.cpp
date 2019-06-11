/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *first = NULL;
    TreeNode *second = NULL;
    TreeNode *pre = NULL;
    void recoverTree(TreeNode* root) {
        help(root);
        if(first && second) {
            int tmp = first->val;
        first->val = second->val;
        second->val = tmp;    
        }
    }
    
    void help(TreeNode* root) {
        if(root == NULL)
            return;
        help(root->left);
        
        if(pre && root->val < pre->val) {
            if(first == NULL) {
                first = pre;
            }
            if(first != NULL) {
                second = root;
            }
        }
        pre = root;
        help(root->right);
    }
};