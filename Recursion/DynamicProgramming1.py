
changes = 63
coins = [1, 5, 10, 25]
knownResults = [None] * (changes + 1)


def recDC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] is not None:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


if __name__ == '__main__':
    print(recDC(coins, changes))
