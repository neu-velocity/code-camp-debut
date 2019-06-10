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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        map<int, vector<int>> hash;
        vector<vector<int>> ret;
        if(root == NULL)
            return ret;
        queue<pair<TreeNode*, int>> q;
        q.push(pair<TreeNode*, int>(root, 0));
        while(!q.empty()) {
            pair<TreeNode*, int> p = q.front();
            q.pop();
            TreeNode *node = p.first;
            if(hash.find(p.second) == hash.end()) {
                hash[p.second] = {node->val};
            }else{
                hash[p.second].push_back(node->val);
            }
            if(node->left) {
                q.push(pair<TreeNode *, int>(node->left, p.second-1));
            }
            if(node->right) {
                q.push(pair<TreeNode *, int>(node->right, p.second+1));
            }
        }
        
        for(auto it = hash.begin(); it != hash.end(); it++) {
            ret.push_back(it->second);
        }
        return ret;
    }
};