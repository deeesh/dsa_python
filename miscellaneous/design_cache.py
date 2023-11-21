# Design a simple cache using a dictionary to store key value pair

from collections import OrderedDict

class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # move the acccessed key at end
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            # Update the value and move the key to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache)>=self.cap:
                self.cache.popitem(last = False)
            self.cache[key] = value


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # Capacity of cache
        cap = int(input())
        # Number of Queries
        qry = int(input())
        # Parent child info in list
        a = list(map(str, input().strip().split()))

        lru = LRUCache(cap)

        i=0
        q=1
        while q<qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i+1]), int(a[i+2]))
                i+=3
            elif qtyp == 'GET':
                print(lru.get(int(a[i+1])), end=" ")
                i+=2
            q+=1
        print()
            


