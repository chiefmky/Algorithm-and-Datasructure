from timeit import Timer

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def Palindrome():
    astr = "radar"
    myDeque = Deque()
    check = True

    for ch in astr:
        myDeque.addRear(ch)

    while myDeque.size() > 1:

        if myDeque.removeFront() != myDeque.removeRear():
            return False

    return check

if __name__ == '__main__':
    n = 10
    t1 = Timer("Palindrome()", "from __main__ import Palindrome")
    print("concat ", t1.timeit(number=n), "milliseconds")
