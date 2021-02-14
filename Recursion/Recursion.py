def listsum(numArr):
    thesum = 0
    if len(numArr) <= 1:
        return numArr[0]
    else:
        return numArr[0] + listsum(numArr[1:])

def palString(mystr):
    mystr= mystr.replace(" ", "" )

    if len(mystr) <=1:
         return mystr[0]

    else:
        return palString(mystr[len(mystr)-1]) + palString(mystr[:len(mystr)-1])


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

#Tower of Hanoi
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


if __name__ == '__main__':
    # print(listsum([2, 5, 8, 9]))
    #print(toStr(19, 16))
    #print(palString("Wassamassaw – a town in South Dakota"))
    moveTower(3, "A", "B", "C")
