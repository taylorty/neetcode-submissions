class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.array = [0 for i in range(self.size)] 

    def add(self, key: int) -> None:
        key = key % self.size
        self.array[key] = 1

    def remove(self, key: int) -> None:
        key = key % self.size
        self.array[key] = 0

    def contains(self, key: int) -> bool:
        key = key % self.size
        return self.array[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)