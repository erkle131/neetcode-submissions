
class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, value: int) -> None:
        new_node = TreeNode(key, value)
        if not self.root:
            self.root = new_node
            return
            
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = new_node
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                cur.value = value
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.value
        return -1

    def getMin(self) -> int:
        node = self.minValueNode(self.root)
        return node.value if node else -1

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.value if cur else -1

    def minValueNode(self, root: TreeNode) -> TreeNode:
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def removeHelper(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key > root.key:
            root.right = self.removeHelper(root.right, key)
        elif key < root.key:
            root.left = self.removeHelper(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.minValueNode(root.right)
                root.key = min_node.key
                root.value = min_node.value
                root.right = self.removeHelper(root.right, min_node.key)
        return root

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
