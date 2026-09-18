class MyHashMap:

    def __init__(self):
        self.myHashMap = {}
        

    def put(self, key: int, value: int) -> None:
        self.myHashMap[key] = value
        

    def get(self, key: int) -> int:
        if key in self.myHashMap:
            return self.myHashMap[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.myHashMap:
            self.myHashMap.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)