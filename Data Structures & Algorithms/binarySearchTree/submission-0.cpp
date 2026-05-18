class TreeMap {
private:
    struct TreeNode {
        int key;
        int value;
        TreeNode* left;
        TreeNode* right;

        TreeNode(int key, int value) : key(key), value(value), left(nullptr), right(nullptr) {}
    };

    TreeNode* root;

public:
    TreeMap() {
        root = nullptr;
    }

    void insert(int key, int val) {
        if (!root) {
            root = new TreeNode(key, val);
            return;
        }

        TreeNode* curr = root;
        while (true) {
            if (key > curr->key) {
                if (!curr->right) {
                    curr->right = new TreeNode(key, val);
                    break;
                }
                curr = curr->right;
            } else if (key < curr->key) {
                if (!curr->left) {
                    curr->left = new TreeNode(key, val);
                    break;
                }
                curr = curr->left;
            } else { // Key is already present, override old value with new val
                curr->value = val;
                break;
            }
        }
    }

    int get(int key) {
        if (!root) return -1;

        TreeNode* curr = root;
        while (curr) {
            if (key > curr->key) {
                curr = curr->right;
            } else if (key < curr->key) {
                curr = curr->left;
            } else {
                return curr->value;
            }
        }
        return -1;
    }

    int getMin() {
        if (!root) return -1;

        TreeNode* curr = root;
        while (curr && curr->left) {
            curr = curr->left;
        }
        return curr->value;
    }

    int getMax() {
        if (!root) return -1;

        TreeNode* curr = root;
        while (curr && curr->right) {
            curr = curr->right;
        }
        return curr->value;
    }

    void remove(int key) {
        TreeNode* parent = nullptr;
        TreeNode* curr = root;

        // Find the node to delete
        while (curr && curr->key != key) {
            parent = curr;
            if (key > curr->key) {
                curr = curr->right;
            } else {
                curr = curr->left;
            }
        }

        if (!curr) return;

        // Node with only one child or no child
        if (!curr->left || !curr->right) {
            TreeNode* child = curr->left ? curr->left : curr->right;
            if (!parent) {
                root = child;
            } else if (parent->left == curr) {
                parent->left = child;
            } else {
                parent->right = child;
            }
        } else {
            // Node with two children
            TreeNode* par = curr;
            TreeNode* successor = curr->right;
            while (successor->left) {
                par = successor;
                successor = successor->left;
            }

            curr->key = successor->key;
            curr->value = successor->value;

            if (par->left == successor) {
                par->left = successor->right;
            } else {
                par->right = successor->right;
            }
        }
    }

    std::vector<int> getInorderKeys() {
        vector<int> res;
        stack<TreeNode*> stack;

        TreeNode* curr = root;

        while (curr || !stack.empty()) {
            while(curr) {
                stack.push(curr);
                curr = curr->left;
            }
            curr = stack.top();
            stack.pop();
            res.push_back(curr->key);
            curr = curr->right;
        }
        return res;
    }
};