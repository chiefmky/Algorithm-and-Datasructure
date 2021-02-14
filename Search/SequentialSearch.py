def sequentialSearch(myarr,numSearch):
    bool = False
    for arr in myarr:
        if numSearch == arr:
            bool = True
    return bool

if __name__ == "__main__":
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 95))
