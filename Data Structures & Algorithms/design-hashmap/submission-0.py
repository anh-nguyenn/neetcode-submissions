class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1: #key in hashmap
            self.data[self.getKeyIdx(key)][1] = value
        else:
            self.data.append([key, value])

    def get(self, key: int) -> int:
        for val in self.data:
            if key == val[0]:
                return val[1]
        return -1
    def remove(self, key: int) -> None:
        if self.get(key) != -1: #key in hashmap
            self.data.pop(self.getKeyIdx(key))
    def getKeyIdx(self,key:int) -> int:
        for i, num in enumerate(self.data):
            if num[0] == key:
                return i
    


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)