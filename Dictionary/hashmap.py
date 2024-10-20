class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, value):
        index = hash(key) % self.size
        self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    def listAll(self):
        for k in self.table:
            print(k)
    
hm=HashMap(10)

hm.put("abc",4)
hm.put("abcd",5)
hm.put("abcde",6)

print(hm.get("dbc"))
print(hm.get("abc"))

hm.listAll()
