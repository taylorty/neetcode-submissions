class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.array = [[] for i in range(self.size)] 

    def add(self, key: int) -> None:
        new_key = key % self.size
        if key not in self.array[new_key]:
            self.array[new_key].append(key)

    def remove(self, key: int) -> None:
        new_key = key % self.size
        if key in self.array[new_key]:
            self.array[new_key].remove(key)

    def contains(self, key: int) -> bool:
        new_key = key % self.size
        return key in self.array[new_key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)