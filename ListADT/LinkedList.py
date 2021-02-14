class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # add from the front
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def reverseL(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next  # Remember next node
            curr.next = prev  # REVERSE! None, first time round.
            prev = curr  # Used in the next iteration.
            curr = next_node  # Move to next node.
        head = prev

    def append(self, item):
        temp = Node(item)
        previous = None
        current = self.head
        while current != None:
            previous = current
            current = current.next
        previous.next = temp

    def insert(self, pos, item):
        temp = Node(item)
        count = 0
        if count == pos:
            temp.next = self.head
            self.head = temp
            return
        previous = None
        current = self.head

        while count <= pos:
            if count == pos:
                temp.next = current
                previous.next = temp
                return
            else:
                previous = current
                current = current.next
            count += 1

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None:
            if current.data == item:
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return print("Deleted")
            else:
                previous = current
                current = current.next
        return print("element not found")

    def pop(self, pos):
        current = self.head
        previous = None
        count = 0
        while current != None:
            if count == pos:
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return print("Deleted")
            else:
                previous = current
                current = current.next
            count += 1
        return print("element not found")

    def pop(self):
        current = self.head
        previous = None

        while current != None:
            current = current.next
            if current.next == None:
                previous.next = None
                return True
            else:
                previous = current


### ORDERLIST
class OrderList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(item)
        if previous == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.next
        return found

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next

        return found


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
