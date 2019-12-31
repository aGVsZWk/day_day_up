def recMCOther(coinValueList, change):
    # 该解法前提条件：coinValueList 为整数倍的，从大到小排列！！！
    minCoins = 0
    for coin in coinValueList:
        use = change // coin
        minCoins += use
        change = change - coin * use

    return minCoins


if __name__ == '__main__':
    print(recMCOther([200, 100, 20, 10, 5, 1], 628))
