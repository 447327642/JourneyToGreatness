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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        int cnt = 0;
        auto p = root;
        while (!s.empty() || p) {
            if (p) {
                s.push(p)   ;
                p = p->left;
            } else {
                p = s.top();
                s.pop();
                cnt += 1;
                if (cnt == k)
                    return p->val;
                p = p->right;
            }
        }
        return -1;
    }
};
