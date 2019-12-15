def recMC(coinList, change):
    knownResult = [0] * (change+1)
    for i in range(1, change+1):    # 注意这里的取不到
        minCoinNums = i
        if i in coinList:
            knownResult[i] = 1
        else:
            for j in [c for c in coinList if c < i]:
                if knownResult[i-j] + 1 < minCoinNums:
                    minCoinNums = knownResult[i-j] + 1
                knownResult[i] = minCoinNums
    return minCoinNums

if __name__ == '__main__':
    print(recMC([1, 5, 21, 10, 25], 63))
