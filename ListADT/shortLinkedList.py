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

    def append(self, item):
        temp = Node(item)
        previous = None
        current = self.head
        while current is not None:
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

        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current == item:
                found = True
            else:
                current = current.next

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None:
            if current == item:
                if previous is None:
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
        while current is not None:
            if count == pos:
                if previous is None:
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

        while current is not None:
            current = current.next
            if current.next is None:
                previous.next = None
                return print("Deleted")
            else:
                previous = current

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    result_tail = l3
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        sumout = (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) // 10

        result_tail.next = ListNode(sumout)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return l3.next
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
