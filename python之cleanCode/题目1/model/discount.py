"""
餐品优惠表
"""


class Discount:
    # 模拟数据库数据
    database = {
        # 餐品 uid 唯一值
        'ITEM0001': {
            # 名称
            'name': '黄焖鸡',
            'price': 18,
        },

        'ITEM0002': {
            # 名称
            'name': '肉夹馍',
            # 价格
            'price': 12,
        },

        'ITEM0003': {
            # 名称
            'name': '凉皮',
            # 价格
            'price': 8,
        },
    }

    @classmethod
    def food_price(cls, food_uid: str) -> int:
        """
        获取某个餐品的价格
        """
        food = cls.database.get(food_uid, None)
        if not food:
            return -1
        else:
            price = food['price']
            return price

    def food_price_half(cls, food_uid: str) -> int:
        """
        获取某个餐品的价格
        """
        food = cls.database.get(food_uid, None)
        if not food:
            return -1
        else:
            price = food['price']
            return price
