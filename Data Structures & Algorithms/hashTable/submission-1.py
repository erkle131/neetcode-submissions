
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [Node(None, None) for _ in range(capacity)]

    def hash_function(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        dummy = self.table[index]
        cur = dummy

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next

        cur.next = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hash_function(key)
        dummy = self.table[index]
        cur = dummy.next

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        dummy = self.table[index]
        cur = dummy

        while cur.next and cur.next.key != key:
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
            self.size -= 1
            return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [Node(None, None) for _ in range(new_capacity)]

        for dummy in self.table:
            cur = dummy.next
            while cur:
                nxt = cur.next
                new_index = cur.key % new_capacity
                cur.next = new_table[new_index].next
                new_table[new_index].next = cur
                cur = nxt

        self.capacity = new_capacity
        self.table = new_table
