from collections import defaultdict

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """A helper class to manage nodes with the same frequency."""
    def __init__(self):
        self.sentinel = ListNode(None, None)  # Dummy head/tail
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        """Adds a node to the end (Most Recently Used for this frequency)."""
        node.next = self.sentinel
        node.prev = self.sentinel.prev
        node.prev.next = node
        self.sentinel.prev = node
        self._size += 1

    def pop(self, node=None):
        """Removes a specific node, or the head (LRU) if none is provided."""
        if self._size == 0:
            return None
        
        if not node:
            node = self.sentinel.next
            
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}  # key -> node
        self.freq_map = defaultdict(DoublyLinkedList)  # freq -> DoublyLinkedList

    def _update_node(self, node):
        """Increments node frequency and moves it to the appropriate list."""
        freq = node.freq
        self.freq_map[freq].pop(node)
        
        # If the min_freq list is now empty, increment min_freq
        if freq == self.min_freq and not self.freq_map[freq]:
            self.min_freq += 1
        
        node.freq += 1
        self.freq_map[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self._update_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update_node(node)
        else:
            if len(self.key_map) >= self.capacity:
                # Evict the Least Recently Used node from the Min Frequency list
                removed_node = self.freq_map[self.min_freq].pop()
                del self.key_map[removed_node.key]

            new_node = ListNode(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].append(new_node)
            self.min_freq = 1