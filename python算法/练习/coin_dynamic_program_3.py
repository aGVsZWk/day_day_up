def recMC(coinList, target):
    knownResult = [0] * (target + 1)
    for i in range(1, target+1):        # 注意这里的 + 1
        minCoins = i
        for j in [c for c in coinList if c <= i]:
            if knownResult[i-j] + 1 < minCoins:
                minCoins = knownResult[i-j] + 1
        knownResult[i] = minCoins

    return knownResult[target]

if __name__ == '__main__':
    print(recMC([1, 5, 21, 10, 25], 63))


# def recMC(coinList, target):
#     knownResult = [i for i in range(target+1)]
#     for i in range(1, target+1):        # 注意这里的 + 1
#         for j in [c for c in coinList if c <= i]:
#             knownResult[i] = min(knownResult[i-j]+1, knownResult[i])
#     return knownResult[target]
#
# if __name__ == '__main__':
#     print(recMC([1, 5, 21, 10, 25], 63))
