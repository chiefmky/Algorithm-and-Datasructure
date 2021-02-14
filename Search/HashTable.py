
hash_tbl = [None] * 11
def hashfunc(item):
    return key % 11

def put(item):
    hash_tbl[hashfunc(item)] = item

def contains(item):
    return hash_tbl[hashfunc(item)] == item


def rehash(self, oldhash, size):
    return (oldhash + 1) % size