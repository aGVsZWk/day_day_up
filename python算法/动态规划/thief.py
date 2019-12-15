def thief(goodsWeightPrice, max_weight):
    goodsWeightPrice.insert(0, None)
    # 生成缓存内容，从 (0, 0) 开始，因为后面有减法差等于 0 的情况
    weight_cache = {(i, j): 0 for i in range(len(goodsWeightPrice)) for j in range(max_weight + 1)}
    # 每件宝物
    for i in range(1, len(goodsWeightPrice)):
        # 重量
        for j in range(1, max_weight + 1):
            # 装不下宝物
            if goodsWeightPrice[i]['w'] > j:
                weight_cache[(i, j)] = weight_cache[(i - 1, j)]
            # 装下宝物，取不装该宝物价值和装了该宝物后的价值的最大值
            else:
                weight_cache[(i, j)] = max(weight_cache[(i - 1, j)], weight_cache[(i - 1, j - goodsWeightPrice[i]['w'])] + goodsWeightPrice[i]['p'])
    return weight_cache[(len(goodsWeightPrice) - 1, max_weight)]


if __name__ == '__main__':
    goodsWeightPrice = [{"w": 2, "p": 3}, {"w": 3, "p": 4}, {"w": 4, "p": 8}, {"w": 5, "p": 8}, {"w": 9, "p": 10}]
    print(thief(goodsWeightPrice, 20))
