def BinarySearch(myarr, item):
    start = 0
    end = len(myarr) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if myarr[middle] == item:
            return True
        else:
            if item > myarr[middle]:
                start = middle + 1
            else:
                end = middle - 1
    return False


def BinarySearch2(myarr, item):
    if len(myarr) == 0:
        return False
    else:
        midpoint = len(myarr) // 2
        if myarr[midpoint] == item:
            return True
        else:
            if item > myarr[midpoint]:
                return BinarySearch2(myarr[midpoint + 1:], item)
            else:
                return BinarySearch2(myarr[:midpoint], item)


def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(BinarySearch2(testlist, 2))
