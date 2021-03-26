class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)

        return  h%self.max
    def __setitem__(self, key, value):
        h=self.get_hash(key)
        self.arr[h]=value
    def __getitem__(self, index):
        h=self.get_hash(index)
        return self.arr[h]
    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None



t=HashTable()
t['jan 2']=7
t['mar 4']=5
t['nov 5']=4
t['jan 6']=3

print(t.arr)
print(len(t.arr))
print(t['mar 4'])