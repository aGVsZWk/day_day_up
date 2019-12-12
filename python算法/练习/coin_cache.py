def recMC(coinValueList, change, knownResults):
    if change in coinValueList:
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    minCoins = change
    for i in [c for c in coinValueList if c < change]:
        numCoins = 1 + recMC(coinValueList, change-i, knownResults)
        if numCoins < minCoins:
            knownResults[change] = numCoins
            minCoins = numCoins
    return minCoins

if __name__ == '__main__':
    print(recMC([1, 5, 10, 25], 63, [0]*64))
