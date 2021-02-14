class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newprevious):
        self.previous = newprevious

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # add from the front
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        temp.setPrevious(self.head)

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        return count


if __name__ == '__main__':
    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist.size())
    mylist.remove(54)
    print(mylist.search(93))
    mylist.remove(100)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))


    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(55)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
