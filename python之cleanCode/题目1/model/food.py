"""
餐品表
"""
from typing import List


class Food:
    # 模拟数据库数据
    database = {
        # 餐品 uid 唯一值
        'ITEM0001': {
            # 名称
            'name': '黄焖鸡',
            # 原价
            'price_original': 18,
            # 折扣价格
            'price_discount': 9,
        },

        'ITEM0013': {
            'name': '肉夹馍',
            'price_original': 6,
            # -1 表示没有优惠价格
            'price_discount': -1,
        },

        'ITEM0022': {
            'name': '凉皮',
            'price_original': 8,
            'price_discount': 4,
        },
    }

    @classmethod
    def food_obj(cls, food_uid: str) -> dict:
        """
        获取某个餐品的实例
        """
        food = cls.database.get(food_uid, None)
        return food

    @classmethod
    def food_name(cls, food_uid: str) -> str:
        """
        获取某个餐品的原价
        """
        food = cls.database.get(food_uid, None)
        if not food:
            return ''
        else:
            n = food['name']
            return n

    @classmethod
    def price_original(cls, food_uid: str) -> int:
        """
        获取某个餐品的原价
        """
        food = cls.database.get(food_uid, None)
        if not food:
            return -1
        else:
            p = food['price_original']
            return p

    @staticmethod
    def price_original_total(food_list: List[dict]) -> int:
        """
        获取餐品列表的原价
        """
        total = 0
        for food in food_list:
            price = food.get('price_original')
            num = food['num']
            total += (price * num)

        return total

    @classmethod
    def price_half(cls, food_uid: str) -> int:
        """
        获取某个餐品的半价优惠价格
        """
        food = cls.database.get(food_uid, None)
        # 判断是否有优惠价格
        has_discount = food['price_discount'] != -1
        if has_discount:
            p = food['price_discount']
            return p
        else:
            p = food['price_original']
            return p
