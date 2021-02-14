def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
    return arr


def quickSortHelper(alist, start, end):
    if start < end:
        mid = randPartition(alist, start, end)
        quickSortHelper(alist, start, mid - 1)
        quickSortHelper(alist, mid + 1, end)


def randPartition(alist, start, end):
    pivot = alist[start]
    left = start + 1
    right = end

    done = False

    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1

        while right >= left and alist[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]

    alist[left], alist[right] = alist[right], alist[left]

    return right


if __name__ == "__main__":
    testlist = [54,26,93,17,77,31,44,55,20]
    print(quickSort(testlist))