
class HashTable:

    def __init__(self, size):
        self.arr = [[] for j in range(size)]
        self.keys = [[] for j in range(size)]

    def resize(self, size):
        newArr = [[] for j in range(size)]
        newKeyArr = [[] for j in range(size)]
        for i in self.keys:
            for j in i:
                val = self.get(j)
                key = j
                newHashedKey = self.hashCode(key, size)
                newArr[newHashedKey].append(val)
                newKeyArr[newHashedKey].append(key)
        self.arr = newArr
        self.keys = newKeyArr




    def put(self, key, value):
        hashedKey = self.hashCode(key, len(self.arr))
        self.keys[hashedKey].append(key)
        self.arr[hashedKey].append(value)

    # def remove(self, key):
    #     hashedKey = hash(key)
    #     self.arr[hashedKey] = None

    def get(self, key):
        hashedKey = self.hashCode(key, len(self.arr))
        for i in range(len(self.keys[hashedKey])):
            if self.keys[hashedKey][i] == key:
                return self.arr[hashedKey][i]
        return None

    def hashCode(self, key, size):
        return hash(key)%size


    # def contains(self, key):
    #     hashedKey = hash(key)
    #     return self.arr[hashedKey] != None

    def double(self):
        numKeys = 0
        for i in range(len(self.arr)):
            numKeys += len(self.arr[i])
        #should get total number of keys based on the length of each array
        if(float(numKeys)/len(self.arr) >= .8):
            self.resize(len(self.arr) * 2)


    def __repr__(self):
        return str(self.arr)



if __name__ == "__main__":
    ht = HashTable(3)
    print('testing put:')
    print('initialized it to size of 4')
    print('i\'m putting 5 values named val1, val2... with corresponding keys called key1, key2...')
    print('this is what the array of values looks like:')
    print('when it collides it puts them into array')
    ht.put("key1", "val1")
    ht.put("key2", "val2")
    ht.put("key3", "val3")
    ht.put("key4", "val4")
    ht.put("key5", "val5")
    print(ht)
    print('testing get:')
    print('getting key3, should be val3',ht.get("key3"))
    print('getting key2, should be val2',ht.get("key2"))

    print('testing resize:')
    ht.resize(10)
    print('resized it to 10, should have length of 10 with values in new slots:')
    print(ht)

    print('testing double:')
    ht.double()
    print('doubled the array, since there are only 5 values and 10 slots, it should NOT double:')
    print(ht)
    ht.put("key6","val6")
    ht.put("key7", "val7")
    ht.put("key8", "val8")
    ht.put("key9", "val9")
    print('put 4 more values/keys into array')
    print('doubled the array, since there are 9 values and 10 slots, it should resize to 20 slots:')
    ht.double()
    print(ht)
