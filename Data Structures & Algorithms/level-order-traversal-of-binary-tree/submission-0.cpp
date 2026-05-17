/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> queue;
        vector<vector<int>> res;

        if (root) {
            queue.push(root);
        }

        while (queue.size() > 0) {
            vector<int> sublist;
            int length = queue.size();

            for (int i = 0; i < length; i++) {
                TreeNode* curr = queue.front();
                queue.pop();

                sublist.push_back(curr->val);

                if (curr->left) queue.push(curr->left);
                if (curr->right) queue.push(curr->right);
            }
            res.push_back(sublist);
            sublist = {};
        }
        return res;
    }
};