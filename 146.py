"""
Answer (deque):
"""
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.orderqueuekey = Deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.map :
            self.orderqueuekey.remove(key)
            self.orderqueuekey.appendleft(key)
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if len(self.orderqueuekey) == self.cap:
                old = self.orderqueuekey.pop()
                del self.map[old]
                self.map[key] = value
                self.orderqueuekey.appendleft(key)
            else:
                

                self.map[key] = value
                self.orderqueuekey.appendleft(key)
        else: 
            self.orderqueuekey.remove(key)   

            self.map[key] = value
            self.orderqueuekey.appendleft(key)

"""
Answer (double linked list):
"""
class LRUCache:

    def __init__(self, capacity):
    def get(self, key):
    def put(self, key, value):

"""
Tests:
"""