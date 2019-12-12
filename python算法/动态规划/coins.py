###
### 递归解决硬币找零问题
###
def recMC(coinValueList, change):
    """
    coinValueList: 硬币分值列表
    change: 要找零的钱数
    """
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


if __name__ == '__main__':
    print(recMC([1, 5, 10, 25], 63))
