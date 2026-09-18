class MyHashSet:

    def __init__(self):
        self.myHashSet = []
        

    def add(self, key: int) -> None:
        if key not in self.myHashSet:
            self.myHashSet.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.myHashSet:
            self.myHashSet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.myHashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)