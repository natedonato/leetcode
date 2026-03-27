class Llist:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self, node):

        if node == self.head:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None 
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = node.prev
            nxt = node.next
            if prev:
                prev.next = nxt
            if nxt:
                nxt.prev = prev
            
    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None

class Listnode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = {}
        self.list = Llist()        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.list.delete(node)
            self.list.append(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.list.delete(node)
            self.list.append(node)
        elif self.size < self.capacity:    
            self.size += 1
            node = Listnode(key, value)
            self.map[key] = node
            self.list.append(node)
        else:
            h = self.list.head
            if h:
                del self.map[h.key]
                self.list.delete(self.list.head)
            node = Listnode(key, value)
            self.map[key] = node
            self.list.append(node)

