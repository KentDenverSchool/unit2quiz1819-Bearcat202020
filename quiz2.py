
class HashTable:

    def __init__(self, size):
        self.arr = [[] for j in range(size)]
        self.keys = [[] for j in range(size)]

    def resize(self, size):
        newArr = [None] * size
        newKeyArr = [None] * size
        for i in self.keys:
            if(i != None):
                val = self.get(i)
                key = i
                newHashedKey = self.hashCode(key)
                newArr[newHashedKey] = val
                newKeyArr[newHashedKey] = key
        self.arr = newArr
        self.keys = newKeyArr




    def put(self, key, value):
        hashedKey = self.hashCode(key)
        print('putting' , key, 'at ', hashedKey)
        self.keys[hashedKey].append(key)
        self.arr[hashedKey].append(value)

    # def remove(self, key):
    #     hashedKey = hash(key)
    #     self.arr[hashedKey] = None

    def get(self, key):
        hashedKey = self.hashCode(key)
        print('grabbing ', key, 'and receiving', hashedKey)
        for i in self.arr[hashedKey]:
            print(i)
            if i == key:
                return i
        return None

    def hashCode(self, key):
        return hash(key)%len(self.arr)


    # def contains(self, key):
    #     hashedKey = hash(key)
    #     return self.arr[hashedKey] != None

    def double():
        numKeys = 0
        for i in range(len(self.arr)):
            numKeys += len(self.arr[i])
        #should get total number of keys based on the length of each array
        if(float(keys)/len(self.arr) > .8):
            self.resize(len(self.arr) * 2)
    def __repr__(self):
        return str(self.arr)
'''
Question 1:
    -a large prime number is better because it is less likely to create patterns when you mod numbers that are factors of the number you are modding by

    i.e.
        6%12 == 6
        12%12 == 0
        18%12 == 6
        24%12 == 0

    whereas a prime number like 11 creates less patterns
        6%11 == 6
        12%11 == 1
        18%11 == 7
        24%11 == 2 ...

Question 2:
    -summing characters is a bad way to hash because it ignores the order of the letters in the string
    -"hello" will be give the same hashed key as "elloh"

Question 3:
    -looking at the Java way of hashing, I think it works like one-way encryption
    -after snooping some more, i found this comment that says the method calculates the hashcode like this
        -s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
    -i believe n is the index of each character in the string





'''

# def myHash(obj):
#     hash = int(obj, 36) * 3803
#     strHash = str(hash)
#     bigPrime = 7949
#     otherBigPrime = 4801
#     num = 0
#
#     for i in range(len(strHash)):
#         if(i%3 == 0):
#             num += int(strHash[i]) * otherBigPrime % bigPrime * i
#         elif (i%3 == 1):
#             num -= int(strHash[i]) * otherBigPrime % bigPrime * i
#         else:
#             num *= int(strHash[i]) * otherBigPrime % bigPrime * i
#
#
#     return int(abs(num)) % 7963


if __name__ == "__main__":
    ht = HashTable(5)
    print('testing put:')

    ht.put("j2", "h")
    ht.put("1", "h1")
    ht.put("jasf", "h2")
    ht.put("asdfj2", "h3")
    ht.put("jfasd2", "h4")
    print(ht)
    print('testing get:')
    print(ht.get("h1"))


    #check other doc for testing
    # testArr = []
    # i = 0
    # firstLetter = 65
    # secondLetter = 65
    # thirdLetter = 65
    # num = 0
    # amountOfIterations = 1000
    # while i < amountOfIterations:
    #     if thirdLetter >= 90:
    #         thirdLetter = 65
    #         secondLetter += 1
    #     elif secondLetter >= 90:
    #         secondLetter = 65
    #         firstLetter += 1
    #     else:
    #         thirdLetter += 1
    #
    #     testStr = chr(firstLetter) + chr(secondLetter) + chr(thirdLetter)
    #
    #     if myHash(testStr) in testArr:
    #         num += 1
    #     testArr.append(myHash(testStr))
    #     i+=1
    # print("percent of collisions is:", num/amountOfIterations * 100, "%")
    #
