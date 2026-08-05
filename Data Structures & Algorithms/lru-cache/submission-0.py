
class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.node_map = {}

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.node_map:
            self.remove(self.node_map[key])
            self.insert(self.node_map[key])
            return self.node_map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(self.node_map[key])
        self.node_map[key] = ListNode(key, value)
        self.insert(self.node_map[key])

        if len(self.node_map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.node_map[lru.key]
            