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
    bool isValidBST(TreeNode* root) {
        if(root == NULL)
            return true;
        stack<TreeNode *> s;
        TreeNode *pre = NULL;
        while(!s.empty() || root) {
            while(root) {
                s.push(root);
                root = root->left;
            }
            if(!s.empty()) {
                root = s.top();
                s.pop();
                if(pre &&pre->val >= root->val) {
                    return false;
                }    
                pre = root;
                root = root->right;
            }
        }
        return true;
    }
};