class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(listName, myCount):
    myQueue = Queue()

    for name in listName:
        myQueue.enqueue(name)

    while myQueue.size() != 1:
        num = myCount
        for x in range(num):
            myQueue.enqueue(myQueue.dequeue())

        myQueue.dequeue()
    return print(myQueue.dequeue())


class MyCircularQueue:

    def __init__(self, k: int):
        self.items = [None] * k
        self.size = k
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.items == []

    def isFull(self):
        return ((self.rear + 1) % self.size) == self.front

    def Front(self):
        if self.front == -1:
            return -1
        else:
            return self.items[self.front]

    def Rear(self):
        if self.rear == -1:
            return -1
        else:
            return self.items[self.rear]

    def enQueue(self, value: int):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.items[self.rear] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return True
        self.front = (self.front + 1) % self.size
        return True

if __name__ == '__main__':
    hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
