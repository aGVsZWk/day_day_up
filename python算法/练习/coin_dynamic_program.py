def recMC(coinValueList, change):
    knowChangeCoins = [0] * (change+1)
    for i in range(1, change+1):
        minCoins = i
        for j in [c for c in coinValueList if c <= i]:
            if knowChangeCoins[i-j] + 1 < minCoins:
                minCoins = knowChangeCoins[i-j] + 1
                knowChangeCoins[i] = minCoins
    return knowChangeCoins[change]

if __name__ == '__main__':
    print(recMC([1, 5, 21, 10, 25], 63))
