class RandomizedSet:

    
    def __init__(self):
        self._lis = set([])
        self.temp = []

    def insert(self, val: int) -> bool:
        if val not in self._lis:
            self._lis.add(val)
            self.temp.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._lis:
            self._lis.remove(val)
            self.temp.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        x = random.randint(0,len(self._lis)-1)
        return self.temp[x]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()