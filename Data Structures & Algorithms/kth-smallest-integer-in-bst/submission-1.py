# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tmp = [k, 0]
        def dfs(root, tmp):
            if not root:
                return

            dfs(root.left, tmp)
            tmp[0] -= 1
            if tmp[0] == 0:
                tmp[1] = root.val
                return
            dfs(root.right, tmp)

        dfs(root, tmp)
        return tmp[1]

