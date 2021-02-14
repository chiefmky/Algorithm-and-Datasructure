class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def reverseString(myStr):
    stack = Stack()

    for ch in myStr:
        stack.push(ch)
    revrs = ""
    for ch in range(stack.size()):
        revrs += stack.pop()

    print(revrs)


def parChecking(myChar):
    stack2 = Stack()
    balance = True

    for ch in myChar:
        if ch in "{([":
            stack2.push(ch)
        else:
            if stack2.isEmpty():
                balance = False
            else:
                top = stack2.pop()
                if not matches(top, ch):
                    return False
    if stack2.isEmpty():
        balance = True
    else:
        balance = False
    return balance


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def baseConverter(myNumber, base):
    remStack = Stack()
    a = ""

    while myNumber > 0:
        rem = myNumber % base
        myNumber = myNumber // base

        remStack.push(rem)

    while not remStack.isEmpty():
        a += str(remStack.pop())

    return a


def solution(mystring):
    stack = Stack()
    i = 0
    a = []

    while i < len(mystr):
        if stack.isEmpty():
            stack.push(mystr[i])
        else:
            if mystr[i] == stack.peek():
                stack.pop()
            else:
                stack.push(mystr[i])
        i += 1

    if stack.isEmpty():
        return print("Khali")
    else:
        while not stack.isEmpty():
            a.append(stack.pop())
    a.reverse()
    return print("".join(a))


def parChecking2(myChar):
    stack2 = Stack()
    count = 0

    for ch in myChar:
        if ch in "(":
            stack2.push(ch)
            count += 1
        if ch in ")":
            if stack2.isEmpty():
                count += 1
            else:
                stack2.pop()
                count -= 1
    return count


if __name__ == "__main__":
    name = input()

    print(parChecking2(name))
