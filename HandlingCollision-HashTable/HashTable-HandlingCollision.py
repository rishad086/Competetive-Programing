class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)] #list-comprehention
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)

        return  h%self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]

t = HashTable()

t["march 6"] = 315
t["march 9"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t.arr)
print(t["march 6"])
del t["march 6"]
print(t.arr)
print(t['march 6'])
