class Pair:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def hash_function(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        while True:
            if self.table[index] == None:
                self.table[index] = Pair(key, value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.table[index].key == key:
                self.table[index].value = value
                return

            index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        start_index = index

        while self.table[index] != None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)

        while self.table[index] != None:
            if self.table[index].key == key:
                self.table[index] = None
                self.size -= 1
                
                # Rehash subsequent elements in the cluster to fill the hole
                next_idx = (index + 1) % self.capacity
                while self.table[next_idx] is not None:
                    pair_to_rehash = self.table[next_idx]
                    self.table[next_idx] = None
                    self.size -= 1
                    self.insert(pair_to_rehash.key, pair_to_rehash.value)
                    next_idx = (next_idx + 1) % self.capacity
                
                return True
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for pair in old_table:
            if pair:
                self.insert(pair.key, pair.value)