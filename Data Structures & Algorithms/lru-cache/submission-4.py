class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.key}: {self.val})"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = defaultdict(Node)
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, head):
        prev = head.prev
        nxt = head.next
        prev.next = nxt
        nxt.prev = prev

    def addToHead(self, node):
        headNext = self.head.next
        headNext.prev = node
        self.head.next = node
        node.next = headNext
        node.prev = self.head

    def get(self, key: int) -> int:
        # print("get", key)
        # print(self.dictionary)
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove(node)
            self.addToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # print("put", key, value)
        # print(self.dictionary)
        if key in self.dictionary:
            node = self.dictionary[key]
            node.val = value
            self.remove(node)
            self.addToHead(node)
        elif len(self.dictionary) < self.capacity:
            self.dictionary[key] = Node(key, value)
            self.addToHead(self.dictionary[key])
        else:
            node = self.tail.prev
            self.remove(node)
            del self.dictionary[node.key]
            self.dictionary[key] = Node(key, value)
            self.addToHead(self.dictionary[key])
        
