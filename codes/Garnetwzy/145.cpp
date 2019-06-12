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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        if(root == NULL)
            return ret;
        stack<TreeNode*> s;
        TreeNode *p = root;
        do{
            while(p) {
                s.push(p);
                p = p->left;
            }
            TreeNode *pre = NULL;
            bool check = true;
            while(!s.empty() && check) {
                if(s.top()->right == pre) {
                    ret.push_back(s.top()->val);
                    pre = s.top();
                    s.pop();
                }else {
                    p = s.top()->right;
                    check = false;
                }
            }
        }while(!s.empty());
        return ret;
    }
};