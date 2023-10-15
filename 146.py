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
    class Node:
        def __init__(self,key,val) :
            self.key = key
            self.val = val
            self.pres = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {} # Key is key and value is Node
        self.tail = self.Node("Tail","Tail")
        self.head = self.Node("Head","Head")
        self.tail.next = self.head
        self.head.pres = self.tail

    def addNode(self,newnode):
        OldNewNode = self.head.pres

        newnode.pres = OldNewNode
        newnode.next = self.head
        self.map[newnode.key] = newnode

        OldNewNode.next = newnode
        self.head.pres = newnode

    def deleteNode(self,oldnode):
        presNode = oldnode.pres
        nextNode = oldnode.next
        presNode.next = nextNode
        nextNode.pres = presNode
        del self.map[oldnode.key]

    def get(self, key):
        if key not in self.map :
            return -1
        # On recup la valeur
        Noderes = self.map[key]
        res = Noderes.val

        # On supprime le Node
        self.deleteNode(Noderes)
        # On ajoute le Node après Head
        self.addNode(Noderes)
        return res

    def put(self, key, value):
        # Si le node existe, tu le supprime
        if key in self.map :
            self.deleteNode(self.map[key])
        # Tu ajoute le nouveau node
        NewNode = self.Node(key,value)
        self.addNode(NewNode)
        # Si trop d'element dans le cache
        if len(self.map)-1 == self.capacity :
            # on supprime le node le plus proche de tail
            self.deleteNode(self.tail.next)


"""
Tests:
"""
