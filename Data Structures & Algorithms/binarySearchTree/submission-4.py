
class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
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
                cur.value = val
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
        node = self.min_value_node(self.root)
        return node.value if node else -1

    def min_value_node(self, root: TreeNode) -> TreeNode:
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.value if cur else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur: TreeNode, key: int) -> TreeNode:
        if not cur:
            return None

        if key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        elif key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            
            min_node = self.min_value_node(cur.right)
            cur.key = min_node.key
            cur.value = min_node.value
            cur.right = self.removeHelper(cur.right, min_node.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)

        inorder(self.root)
        return res
