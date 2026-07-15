class LinkedList:
    
    def __init__(self):
        self.ll = []
    
    def get(self, index: int) -> int:
        if index > len(self.ll) - 1:
            return -1
        return self.ll[index]

    def insertHead(self, val: int) -> None:
        self.ll.insert(0, val)
    def insertTail(self, val: int) -> None:
        self.ll.append(val)

    def remove(self, index: int) -> bool:
        if index > len(self.ll) - 1:
            return False
        print(self.ll)
        del self.ll[index]
        return True

    def getValues(self) -> List[int]:
        return self.ll

    def isEmpty(self):
        return len(self.ll) == 0
        
