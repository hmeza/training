from typing import Optional
from math import floor


class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            self.values[self.index_of(key)] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            return self.values[self.index_of(key)]
        except ValueError:
            return -1

    def remove(self, key: int) -> None:
        try:
            index = self.index_of(key)
            del self.values[index]
            del self.keys[index]
        except ValueError:
            ...

    def index_of(self, key):
        return self.keys.index(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

